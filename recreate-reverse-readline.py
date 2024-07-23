from monty.io import reverse_readline


with open("sample_windows.txt", "w", newline="\r\n") as f:
    f.write("\r\n".join(["Line1", "Line2", "Line3"]))

with open("sample_unix_mac.txt", "w", newline="\n") as f:
    f.write("\n".join(["Line1", "Line2", "Line3"]))

for filename in ("sample_windows.txt", "sample_unix_mac.txt"):
    print(f"Reading file: {filename}")
    with open(filename) as file:
        for line in reverse_readline(file):
            print(repr(line))
