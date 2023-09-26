inp_str = 'bbbwwweeerrrtttyy'
out_str, count, target_char = '', 0, inp_str[0]

for x in inp_str:
    if x == target_char:
        count += 1
        continue
    else:
        out_str = out_str + target_char + str(count)
        count, target_char = 1, x
        continue

out_str = out_str + target_char + str(count)
print(out_str)

