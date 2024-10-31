def get_cats_info(path: str) -> list:
    cats_info = []

    try:
        with open(path, mode="r", encoding="UTF-8") as f:
            records = [record.strip().split(",") for record in f.readlines()]
    except Exception as e:
        return [None, e]

    for [id, name, age] in records:
        cats_info.append({"id": id, "name": name, "age": age})

    return cats_info


if __name__ == "__main__":
    cats_info = get_cats_info("./data/cats.txt")
    if cats_info[0]:
        print(cats_info)
    else:
        print(cats_info[1])
