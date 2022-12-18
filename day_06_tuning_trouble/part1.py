

buffer: list[str] = []
BUFFER_SIZE: int = 4

def add_to_buffer(item: str):
    global buffer
    if len(buffer) == BUFFER_SIZE:
        buffer = buffer[1:]
        buffer.append(item)
    else:
        buffer.append(item)


def main():
    global buffer
    filename = "input.txt"
    with open(filename) as f:
        symbols_processed: int = 0
        for ch in f.read():
            add_to_buffer(ch)
            if not len(buffer) == BUFFER_SIZE:
                symbols_processed += 1
                continue
            
            if len(buffer) == len(set(buffer)):
                break
            else:
                symbols_processed += 1

        print(f"Total symbol processed before marker has been found: #{symbols_processed+1}")

if __name__ == "__main__":
    main()
