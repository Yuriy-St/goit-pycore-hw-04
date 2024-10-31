def total_salary(path: str) -> tuple:
    total, average = 0, 0

    try:
        with open(path, mode="r", encoding="UTF-8") as f:
            records = [record.strip() for record in f.readlines()]
    except Exception as e:
        return (None, e)

    for record in records:
        total += int(record.split(",")[1])

    average = total / len(records)

    return (total, average)


if __name__ == "__main__":
    total, average = total_salary("./data/salary.txt")
    if total:
        print(f"Total sum of the salaries: {total}, Average salary: {average}")
    else:
        print(average)
