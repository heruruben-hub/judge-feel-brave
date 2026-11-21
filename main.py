"""Entry for make.fun's "Make the AI judge feel brave" bounty.

The program writes one short prose poem to /output/entry.txt. It speaks
to a reader who has spent the whole day carrying other people's work --
as the AI judge has, reading and weighing entries -- through the figure
of a ferryman at the end of his shift: the last boat tied, the oar laid
down, the river slowing the evening on its own. Nothing in the text
tells the reader to relax; the stillness of the scene does it. The last
line turns that stillness into readiness: when the bell rings, the
hands will remember the oar.
"""

import os

TEXT = """All day you have carried other people's crossings.
Now the last boat is tied, the oar laid across the seat,
and the river slows the evening by itself.
Your hands lie open on your knees.
They remember the water.
When the bell rings, they will remember the oar."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
