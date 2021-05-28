"""
Perform various operation on list.

Input format:
Number of operations
insert i e: At position i, insert integer e.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""


def convert(text):
    return text.split()


def solution(numbers, commands):
    for command in commands:
        command = convert(command)
        if command[0] == 'insert':
            index, item = int(command[1]), int(command[2])
            numbers.insert(index, item)
        elif command[0] == 'append':
            item = int(command[1])
            numbers.append(item)
        elif command[0] == 'remove':
            item = int(command[1])
            for i, number in enumerate(numbers):
                if number == item:
                    del numbers[i]
                    break
        elif command[0] == 'pop':
            numbers.pop()
        elif command[0] == 'sort':
            numbers.sort()
        elif command[0] == 'reverse':
            numbers.reverse()
        elif command[0] == 'print':
            print(numbers)


if __name__ == '__main__':
    commands0 = [
        'insert 0 5',
        'insert 1 10',
        'insert 0 6',
        'print',
        'remove 6',
        'append 9',
        'append 1',
        'sort',
        'print',
        'pop',
        'reverse',
        'print'
    ]
    commands1 = [
        'append 1',
        'append 6',
        'append 10',
        'append 8',
        'append 9',
        'append 2',
        'append 12',
        'append 7',
        'append 3',
        'append 5',
        'insert 8 66',
        'insert 1 30',
        'insert 6 75',
        'insert 4 44',
        'insert 9 67',
        'insert 2 44',
        'insert 9 21',
        'insert 8 87',
        'insert 1 75',
        'insert 1 48',
        'print',
        'reverse',
        'print',
        'sort',
        'print',
        'append 2',
        'append 5',
        'remove 2',
        'print',
    ]
    comands_list = [commands0, commands1]

    for commands in comands_list:
        numbers = list()
        solution(numbers, commands)
