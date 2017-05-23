from collections import OrderedDict


def _build_counts_map(string):
    counts_map = OrderedDict()
    for char in string:
        if char in counts_map:
            counts_map[char] += 1
        else:
            counts_map[char] = 1
    return counts_map


def find_permutations(string):
    if string is None or string == '':
        return string
    counts_map = _build_counts_map(string)
    curr_results = []
    results = []
    _find_permutations(counts_map, curr_results, results, len(string))
    return results


def _find_permutations(counts_map, curr_result,
                       results, input_length):
    for char in counts_map:
        if counts_map[char] == 0:
            continue
        curr_result.append(char)
        counts_map[char] -= 1
        if len(curr_result) == input_length:
            results.append(''.join(curr_result))
        else:
            _find_permutations(counts_map, curr_result,
                                    results, input_length)
        counts_map[char] += 1
        curr_result.pop()