import queue

def parseLinkFile(fileName):
    links = queue.Queue()
    lf = open(fileName)
    for line in lf:
        links.put(line.strip())
    lf.close()
    return links
