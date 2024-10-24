import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Ubah daftar menjadi numpy array 3x3
    array = np.array(lst).reshape(3, 3)
    
    # Hitung nilai rata-rata, varians, deviasi standar, maksimum, minimum, dan jumlah
    mean = [list(np.mean(array, axis=0)), list(np.mean(array, axis=1)), np.mean(array)]
    variance = [list(np.var(array, axis=0)), list(np.var(array, axis=1)), np.var(array)]
    std_dev = [list(np.std(array, axis=0)), list(np.std(array, axis=1)), np.std(array)]
    max_val = [list(np.max(array, axis=0)), list(np.max(array, axis=1)), np.max(array)]
    min_val = [list(np.min(array, axis=0)), list(np.min(array, axis=1)), np.min(array)]
    total = [list(np.sum(array, axis=0)), list(np.sum(array, axis=1)), np.sum(array)]

    # Buat kamus hasil
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': total
    }

    return result
