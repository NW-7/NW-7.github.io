from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


def read_genbank(file_path):
    records = []
    with open(file_path, "r") as handle:
        for record in SeqIO.parse(handle, "genbank"):
            sequence = str(record.seq).upper()  # Последовательность в верхнем регистре
            gc = gc_fraction(sequence)
            description = " ".join(record.description.split())            
            records.append((gc, sequence, record.id,description))
    return records


def main():
    file_path = "sequence.gb.txt"
    records = read_genbank(file_path)

    # Сортировка по возрастанию GC-состава
    sorted_records = sorted(records, key=lambda x: x[0])

    # Вывод результатов
    for gc, seq, seq_id, description in sorted_records:
        print(f"{seq_id}: {description}, GC = {gc}")
        print(f"Последовательность (первые 50 символов): {seq[:50]}...\n")
        
if __name__ == "__main__":
    main()
