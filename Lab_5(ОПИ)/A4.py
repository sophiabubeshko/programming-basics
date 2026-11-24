proteins = {}

with open('sequences.0.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split('\t')
        if len(parts) >= 3:
            name = parts[0]
            organism = parts[1]
            seq = parts[2]
            proteins[name] = [organism, seq]

with open('commands.0.txt', 'r', encoding='utf-8') as file:
    commands = file.readlines()

results = []
counter = 1

for cmd in commands:
    cmd = cmd.strip()
    if cmd == "":
        continue

    parts = cmd.split('\t') if '\t' in cmd else cmd.split()
    action = parts[0]

    num_str = str(counter)
    while len(num_str) < 3:
        num_str = "0" + num_str

    if action == 'search':
        target = parts[1]
        results.append(num_str + " search " + target)
        found = False
        for name in proteins:
            if target in proteins[name][1]:
                results.append("organism\t\tprotein")
                results.append(proteins[name][0] + "\t" + name)
                found = True
        if not found:
            results.append("organism\t\tprotein")
            results.append("NOT FOUND")

    elif action == 'diff':
        p1 = parts[1]
        p2 = parts[2]
        results.append(num_str + " diff\t" + p1 + "\t" + p2)

        if p1 not in proteins or p2 not in proteins:
            results.append("amino-acids difference:")
            results.append("MISSING")
        else:
            seq1 = proteins[p1][1]
            seq2 = proteins[p2][1]
            diff_count = 0
            min_len = min(len(seq1), len(seq2))
            for i in range(min_len):
                if seq1[i] != seq2[i]:
                    diff_count += 1
            diff_count += max(len(seq1), len(seq2)) - min_len

            results.append("amino-acids difference:")
            results.append(str(diff_count))

    elif action == 'mode':
        target = parts[1]
        results.append(num_str + " mode\t" + target)

        if target not in proteins:
            results.append("MISSING: " + target)
        else:
            seq = proteins[target][1]
            max_count = 0
            best_letter = ""

            for letter in seq:
                count = seq.count(letter)
                if count > max_count:
                    max_count = count
                    best_letter = letter
                elif count == max_count and letter < best_letter:
                    best_letter = letter

            results.append("amino-acid occurs:")
            results.append(best_letter + "\t\t" + str(max_count))

    results.append("-" * 70)
    counter = counter + 1

with open('genedata.txt', 'w', encoding='utf-8') as file:
    file.write("София Бубешко\n")
    file.write("Genetic Searching\n")
    file.write("-" * 70 + "\n")
    for line in results:
        file.write(line + "\n")

print("Готово! Результаты в файле genedata.txt")