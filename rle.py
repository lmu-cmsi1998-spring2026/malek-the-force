def rle(input):
    if not isinstance(input, (list, str)):
        raise Exception('Invalid input type for RLE. Requires List or String type.')
    if len(input) < 6:
        raise Exception('Input is too short for RLE.')

    output = []
    current_char = input[0]
    count = 1

    for i in range(1, len(input)):
        if input[i] == current_char:
            count += 1
        else:
            if count > 1:
                output.append(count)
            output.append(count)
            output.append(current_char)
            current_char = input[i]
            count = 1

    output.append(count)
    output.append(current_char)
    return output
