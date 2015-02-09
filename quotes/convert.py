
f = open('fortunes','r')
lines = f.readlines()
f.close()



length = len(lines)

i=0
while i < length:
    quote = ""
    while lines[i][0] != '%':
        quote = quote + " " + lines[i].strip();
        i = i+1
    i = i+1
    print quote


for line in lines:
    quote = ""
    if line[0] == '%':
        continue
    else:
        line = line.strip()
        print line

