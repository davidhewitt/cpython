import io
import os

THIS_DIR = os.path.dirname(__file__)

# Physical discussion of surrogateescape error handler
#
# # 4 invalid utf-8 bytes to test surrogateescape error handler
# raw = b"\x80\x80\x80\x80"
# raw_str = raw.decode(errors="surrogateescape")
# # '\udc80\udc80\udc80\udc80'
# print(raw_str.encode(errors="surrogateescape"))


def utf8_copy():
    out = io.StringIO()
    with open(
        os.path.join(THIS_DIR, "data", "pg17989.txt"),
        newline="\n",
    ) as f:
        while chunk := f.read(8192):
            out.write(chunk)
        # TODO: make this newline-based route as efficient too
        # out.writelines(f)
        assert len(out.getvalue()) > 0


if __name__ == "__main__":
    for _ in range(1000):
        utf8_copy()
    print("done")
