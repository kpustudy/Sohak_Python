def main():
    score = int(input("Enter yout score:"))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
if __name__ == "__main__":
    main()


def main():
    number = int(input("입력된 정수는:"))
    if number > 0:
        print("양수입니다")
    elif number < 0:
        print("음수입니다")
    else:
        print("0입니다")
if __name__ == "__main__":
    main()