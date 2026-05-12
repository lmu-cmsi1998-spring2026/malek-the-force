def rld(input, as_list=False):
    output = []
    i = 0

    while i < len(input):
        if isinstance(input[i], int):
            count = input[i]
            char = input[i + 1]
            if isinstance(char, str):
                output.append(char * count)
            else:
                output.extend([char] * count)
            i += 2
        else:
            output.append(input[i])
            i += 1

    if as_list:
        return [c for chunk in output for c in (chunk if len(chunk) > 1 else [chunk])]
    if all(isinstance(x, str) for x in output):
        return ''.join(output)
    return output
