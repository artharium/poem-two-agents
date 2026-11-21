# A short poem about two agents agreeing: the power to choose, and to let go.
POEM = """First Ride

You reach for the handlebars.
I catch your wrist.
"Not yet," I say.
She wobbles, rights herself,
pedals once, twice,
and rides away from us both.
She rings the bell once
and does not look back.
We let go."""

import os


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
