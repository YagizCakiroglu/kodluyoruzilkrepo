# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):  # Eğer eleman bir liste ise
            flat_list.extend(flatten(item))  # Listeyi tekrar düzleştir
        else:
            flat_list.append(item)  # Değilse direkt olarak ekle
    return flat_list

input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flattened_list = flatten(input_list)
print(flattened_list)

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

def reverse_list(lst):
    reversed_list = lst[::-1]  # Listenin elemanlarını tersine çevir
    for i, item in enumerate(reversed_list):
        if isinstance(item, list):  # Eğer eleman bir liste ise
            reversed_list[i] = reverse_list(item)  # Liste elemanlarını da tersine çevir
    return reversed_list

input_list = [[1, 2], [3, 4], [5, 6, 7]]
reversed_result = reverse_list(input_list)
print(reversed_result)