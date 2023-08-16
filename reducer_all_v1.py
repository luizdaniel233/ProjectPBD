import sys
import re

counting = dict()
for line in sys.stdin:
    line = line.strip().lower()

    word, count = line.split('\t', 1)
    word = re.sub(r"[,.?!;:()\[\]{}-]", '', word).replace("'", '').replace('"', '')
    
    try:
        quantity = int(count)
        if word in counting:
            counting[word] += quantity
        else:
            counting[word] = quantity
    except ValueError:
        continue

ordered_counting = sorted(counting.items(), key=lambda x: x[1], reverse=True)

# valores mínimos e máximos de frequência
min_freq = ordered_counting[-1][1]
max_freq = ordered_counting[0][1]

# número de intervalos
num_intervals = 10  

interval_size = (max_freq - min_freq) / num_intervals

histogram = [0] * num_intervals

for _, freq in ordered_counting:
    interval_index = int((freq - min_freq) // interval_size)
    interval_index = min(interval_index, num_intervals - 1)
    histogram[interval_index] += 1

# histograma textual
for i, freq_count in enumerate(histogram):
    interval_start = int(min_freq + i * interval_size)
    interval_end = int(min_freq + (i + 1) * interval_size - 1)
    print(f"Intervalo {i+1} ({interval_start}-{interval_end}) - {freq_count} palavras")

print(f"Palavras Distintas Total: {len(ordered_counting)}")
print(f"Ranking Top 10: {list(ordered_counting)[:10]}")