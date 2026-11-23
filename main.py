#!/usr/bin/env python3
"""Entry program: copy the entry image to /output/entry.png.

The image (entry.png, in this repository) sums up the world's news of
Monday 23 November 2026. The copy is byte for byte, so repeated runs
write identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
