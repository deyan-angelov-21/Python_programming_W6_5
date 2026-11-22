def readNumbers(Filename: str) -> str:
    with open(Filename, "r", encoding="UTF-8") as file:
        Content = file.read()
    return Content

def analyzeNumbers(Content: str) -> str:
    Count = 0
    Total = 0
    Greatest = 0
    for Row in Content.splitlines():
        Number = int(Row)
        Count += 1
        Total += Number
        if Number > Greatest:
            Greatest = Number
    Average = Total / Count
    Results = f"{Count};{Total};{Greatest};{Average:.2f}"
    return Results

def showResults(Filename: str, Results: str) -> None:
    print("#### Number analysis - START ####")
    print(f'File "{Filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(Results)
    print("#### Number analysis - END ####")

def main() -> None:
    print("Program starting.")
    Filename = input("Insert filename: ")
    Content = readNumbers(Filename)
    Results = analyzeNumbers(Content)
    showResults(Filename, Results)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
