import random
import string
import time
from dataclasses import dataclass
from itertools import combinations

import chirper


if __name__ == "__main__":
    random.seed(42)
    NUM_CHIRPS = 100
    CHIRP_LENGTH = 60
    chirps = []

    # Generate original chirps
    for i in range(NUM_CHIRPS):
        content = "".join(random.choices(string.ascii_letters, k=CHIRP_LENGTH))
        chirps.append(chirper.Chirp(i, content))

    # Generate spam
    for i in range(1, 99, 13):
        base_chirp = chirps[i]
        chirps.append(chirper.Chirp(i, base_chirp.content))

    t0 = time.time()
    spammers = chirper.identify_spam(chirps, 3)
    t = time.time() - t0
    print(
        f"The spammers are: {spammers}. Detection using PyO3 and Rust took {t} seconds."
    )
