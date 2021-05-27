"""
Input:
4
bcdef
abcdefg
bcde
bcdef

Output:
3
2 1 1

Explanation:
There are 3 distinct words. Here, "bcdef" appears twice in the input.
The other words appear once each.
"""


def solution(words):
    words_count = dict()

    for word in words:
        if word not in words_count:
            words_count[word] = 1
        else:
            words_count[word] += 1

    output = str()

    for i, key in enumerate(words_count):
        # If this is not the last item
        if i != len(words_count) - 1:
            output += str(words_count[key]) + ' '
        else:
            output += str(words_count[key])

    return len(words_count), output


if __name__ == '__main__':
    words = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
    n, output = solution(words)
    print(n)
    print(output)
