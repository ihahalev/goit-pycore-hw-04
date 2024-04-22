def get_cats_info(path: str) -> tuple[int]:
    try:
        with open(path, "r", encoding='utf-8') as file:
            records = [record.strip() for record in file.readlines()  if record.strip()]
        cats_info = []
        for rec in records:
            id, name, age = rec.split(',')
            cats_info.append({'id':id, 'name':name, 'age':age})
        return cats_info
    except FileNotFoundError:
        print("get_cats_info FileNotFoundError")
        return []
    except Exception as error:
        print("get_cats_info error", type(error), error)
        return []

cats_info = get_cats_info("./02_cats.txt")
if (len(cats_info)):
    print(cats_info)