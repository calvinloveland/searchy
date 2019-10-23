import sys
import os

ingestDir = sys.argv[1]
print("Ingesting at: " + ingestDir)
files = [f for f in os.listdir(ingestDir) if os.path.isfile(os.path.join(ingestDir, f))]

print("Found " + str(len(files)) + " files")
print("Starting at: " + files[0])



