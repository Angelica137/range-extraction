def range_extraction(args: list) -> str:
    solution = []
    start = args[0]
    end = args[0]
    for i in args[1:]:
        if i == end + 1:
            end = i
        else:
            if end == start + 1:
                solution.append(str(start))
                solution.append(str(end))
            elif end == start:
                solution.append(str(start))
            else:
                solution.append(f"{start}-{end}")
            start = end = i
    if end == start:
        solution.append(str(start))
    elif end == start + 1:
        solution.append(str(start))
        solution.append(str(end))
    else:
        solution.append(f"{start}-{end}")
    return ",".join(solution)
