if __name__ == "__main__":
    grade_book = dict()
    grades = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade_book[name] = score
        grades.add(score)
    grades = list(grades)
    grades = sorted(grades)
    people = []
    for i in range(len(grade_book)):
        try:
            people.append(
                list(grade_book.keys())[list(grade_book.values()).index(grades[1])]
            )
            grade_book.pop(
                list(grade_book.keys())[list(grade_book.values()).index(grades[1])]
            )
        except:
            break
    people = sorted(people)
    for i in people:
        print(i)
