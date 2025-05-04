
def calculate_gc(sequence):
    gc = sequence.count("G") + sequence.count("C")
    total = len(sequence)
    return (gc / total) * 100 if total > 0 else 0.0


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, "r") as file:
            content = file.read().strip()
    else:
        content = sys.stdin.read().strip()

    records = content.split(">")[1:]

    max_gc = -1.0
    max_id = ""

    for record in records:
        lines = record.split("\n")
        header = lines[0].strip()
        sequence = "".join(line.strip() for line in lines[1:] if line.strip()).upper()

        gc_percent = calculate_gc(sequence)

        if gc_percent > max_gc:
            max_gc = gc_percent
            max_id = header

    print(max_id)
    print(f"{max_gc:.6f}")


if __name__ == "__main__":
    main()
