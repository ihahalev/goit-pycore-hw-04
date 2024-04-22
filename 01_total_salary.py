def total_salary(path: str) -> tuple[int]:
    try:
        with open(path, "r", encoding='utf-8') as file:
            records = [record.strip() for record in file.readlines()  if record.strip()]
        total = 0
        for rec in records:
            _, salary = rec.split(',')
            if salary:
                total += int(salary)
        average = total//len(records)
        return total, average
    except FileNotFoundError:
        print("total_salary FileNotFoundError")
        return 0,0
    except Exception as error:
        print("total_salary error", type(error), error)
        return 0,0

total, average = total_salary("./01_developers.txt")

if (total and average):
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
