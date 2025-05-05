from Bio import SeqIO
from Bio.SeqFeature import CompoundLocation


def format_location(feature):
    """Форматирует локацию в стиле GenBank"""
    if isinstance(feature.location, CompoundLocation):
        parts = [f"{part.start + 1}:{part.end}" for part in feature.location.parts]
        return f"join({', '.join(parts)})"
    return f"{feature.location.start + 1}:{feature.location.end}"


def get_translation(feature):
    """Извлекает перевод из квалификаторов или возвращает None"""
    translation = feature.qualifiers.get("translation", [None])[0]

    if translation:
        # Объединяем многострочные переводы и удаляем пробелы
        return "".join(translation.split())
    return None


def main():
    for record in SeqIO.parse("sequence.gb.txt", "genbank"):
        print(f"{record.id}: {record.description}")

        for i, feature in enumerate(record.features, 1):
            if feature.type == "CDS":
                # Извлекаем информацию из квалификаторов
                strand = "+" if feature.location.strand >= 0 else "-"
                protein_id = feature.qualifiers.get("protein_id", ["unknown"])[0]
                product = feature.qualifiers.get("product", ["unknown"])[0]

                # Получаем готовый перевод или вычисляем
                translation = get_translation(feature)

                print(f"\nCDS {i}: {product} (Protein ID: {protein_id})")
                print(f"Location: [{format_location(feature)}]({strand})")
                print(f"Translation:\n{translation}\n")


if __name__ == "__main__":
    main()