use itertools::Itertools;
use rayon::iter::ParallelBridge;
use rayon::prelude::*;
use std::collections::HashSet;

#[derive(Clone, Debug, Default, Eq, PartialEq)]
pub struct Chirp {
    author_id: usize,
    content: String,
}

impl Chirp {
    pub fn new(author_id: usize, content: String) -> Self {
        Self { author_id, content }
    }
}

fn levenshtein(a: &str, b: &str) -> usize {
    let mut result = 0;

    if a == b {
        return result;
    }

    let length_a = a.chars().count();
    let length_b = b.chars().count();

    if length_a == 0 {
        return length_b;
    }

    if length_b == 0 {
        return length_a;
    }

    let mut cache: Vec<usize> = (1..).take(length_a).collect();
    let mut distance_a;
    let mut distance_b;

    for (index_b, code_b) in b.chars().enumerate() {
        result = index_b;
        distance_a = index_b;
        for (index_a, code_a) in a.chars().enumerate() {
            distance_b = if code_a == code_b {
                distance_a
            } else {
                distance_a + 1
            };
            distance_a = cache[index_a];
            result = if distance_a > result {
                if distance_b > result {
                    result + 1
                } else {
                    distance_b
                }
            } else if distance_b > distance_a {
                distance_a + 1
            } else {
                distance_b
            };
            cache[index_a] = result;
        }
    }
    result
}

pub fn identify_spam(chirps: Vec<Chirp>, threshold: usize) -> HashSet<usize> {
    chirps
        .into_iter()
        .tuple_combinations()
        .par_bridge() // The GIL makes this impossible in Python.
        .map(|(a, b)| {
            (
                levenshtein(a.content.as_str(), b.content.as_str()),
                a.author_id,
                b.author_id,
            )
        })
        .filter(|(dist, _a_id, _b_id)| (*dist) < threshold)
        .flat_map(|(_dist, a_id, b_id)| [a_id, b_id])
        .collect()
}
