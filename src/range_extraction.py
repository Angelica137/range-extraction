def range_extraction(args: list) -> str:
    solution = []
    start = end = args[0]
    for i in args[1:]:
        if i == end + 1:
            end = i
        else:
            append_string(start, end, solution)
            start = end = i
    append_string(start, end, solution)
    return ",".join(solution)


def append_string(start, end, solution) -> list:
    if end == start + 1:
        solution.append(str(start))
        solution.append(str(end))
    elif end == start:
        solution.append(str(start))
    else:
        solution.append(f"{start}-{end}")
