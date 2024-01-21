import random
import string
import time
from dataclasses import dataclass
from itertools import combinations


@dataclass
class Chirp:
    author_id: int
    content: str


def levenshtein(a, b):
    len_1 = len(a) + 1
    len_2 = len(b) + 1

    d = [0] * (len_1 * len_2)

    for i in range(len_1):
        d[i] = i
    for j in range(len_2):
        d[j * len_1] = j

    for j in range(1, len_2):
        for i in range(1, len_1):
            if a[i - 1] == b[j - 1]:
                d[i + j * len_1] = d[i - 1 + (j - 1) * len_1]
            else:
                d[i + j * len_1] = min(
                    d[i - 1 + j * len_1] + 1,
                    d[i + (j - 1) * len_1] + 1,
                    d[i - 1 + (j - 1) * len_1] + 1,
                )

    return d[-1]


def identify_spam(chirps: list[Chirp], threshold: int) -> set[int]:
    spammers = set()
    for chirp_1, chirp_2 in combinations(chirps, 2):
        distance = levenshtein(chirp_1.content, chirp_2.content)
        if distance < threshold:
            spammers.add(chirp_1.author_id)
            spammers.add(chirp_2.author_id)
    return spammers


if __name__ == "__main__":
    random.seed(42)
    NUM_CHIRPS = 100
    CHIRP_LENGTH = 60
    chirps = []

    # Generate original chirps
    for i in range(NUM_CHIRPS):
        content = "".join(random.choices(string.ascii_letters, k=CHIRP_LENGTH))
        chirps.append(Chirp(i, content))

    # Generate spam
    for i in range(1, 99, 13):
        base_chirp = chirps[i]
        chirps.append(Chirp(i + 89, base_chirp.content))

    t0 = time.time()
    spammers = identify_spam(chirps, 3)
    t = time.time() - t0
    print(
        f"The spammers are: {spammers}. Detection using pure Python took {t} seconds."
    )
