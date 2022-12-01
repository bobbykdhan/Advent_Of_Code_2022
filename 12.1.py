def main():
    elf_list = []
    input_data = open("12.1.txt", "r")
    current_elf = 0

    for line in input_data:
        line = line.strip()
        if line == "":
            elf_list.append(current_elf)
            current_elf = 0
            line = "0"

        current_elf += int(line)

    elf_list.sort()

    print("The elf with the largest inventory is " + str(elf_list[len(elf_list) - 1]))
    print("The elf with the 2nd largest inventory is " + str(elf_list[len(elf_list) - 2]))
    print("The elf with the 3rd largest inventory is " + str(elf_list[len(elf_list) - 3]))

    total = elf_list[len(elf_list) - 1] + elf_list[len(elf_list) - 2] + elf_list[len(elf_list) - 3]
    print("The total of these 3 are " + str(total))


if __name__ == '__main__':
    main()
