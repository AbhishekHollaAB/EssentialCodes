import pandas as pd

readXL = pd.read_csv(r'\\10.15.1.24\software department\Abhi\Dates\2024\June\11\Images.csv')
crackIDList = list(readXL['CrackID'])

def countUniqueElements(elements):
    element_counts = {}
    for element in elements:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1
    unique_elements_count = len(element_counts)
    
    return unique_elements_count, element_counts

elements = crackIDList
unique_count, counts = countUniqueElements(elements)
print("Counts of each element:")
for element, count in counts.items():
    print(f"{element}: {count}")
