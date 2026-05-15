import functions

print()

while True:
    try:
        while True:
            functions.getroom()
    except KeyboardInterrupt:
        functions.goodbye()