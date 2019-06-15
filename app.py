import re


def parse():
    targets = []
    sources = []
    exp_source = re.compile(r"\bsource.+")
    exp_target = re.compile(r"\btarget.+")
    exp_separator = re.compile("\"")
    text_file = open("sec.txt", "r")
    print("search started")
    for line in text_file.readlines():
        if exp_target.search(line):
            trgt = exp_target.search(line).group()
            tar = exp_separator.split(trgt)
            target = tar[1]
            targets.append(target)

        if exp_source.search(line):
            src = exp_source.search(line).group()
            sour = exp_separator.split(src)
            source = sour[1]
            sources.append(source)

    sources_and_targets = [
        sources,
        targets
    ]
    text_file.close()
    return sources_and_targets


node_name = input("Write the node name: ")
src_trg = parse()
i = 0
indexes = []

for sourc in src_trg[0]:

    if sourc == node_name:

        indexes.append(i)

    i = i + 1

print(len(indexes))
print("Searched source node: " + node_name)
for index in indexes:
    print("Target node: " + src_trg[1][index])
