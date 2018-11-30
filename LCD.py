from flask import Flask
app = Flask(__name__)


def drawer(n):
    stri = ""
    row = 1
    position = 1
    for i in range(3):
        for j in str(n):
            if j == "0":
                if row == 1:
                    stri += "._."
                if row == 2:
                    stri += "|.|"
                if row == 3:
                    stri += "|_|"
                if position < len(str(n)):
                    stri += " "
                    position += 1
            if j == "1":
                if row == 1:
                    stri += "..."
                if row == 2:
                    stri += "..|"
                if row == 3:
                    stri += "..|"
                if position < len(str(n)):
                    stri += " "
                    position += 1
            if j == "2":
                if row == 1:
                    stri += "._."
                if row == 2:
                    stri += "._|"
                if row == 3:
                    stri += "|_."
                if position < len(str(n)):
                    stri += " "
                    position += 1
            if j == "3":
                if row == 1:
                    stri += "._."
                if row == 2:
                    stri += "._|"
                if row == 3:
                    stri += "._|"
                if position < len(str(n)):
                    stri += " "
                    position += 1
            if j == "4":
                if row == 1:
                    stri += "..."
                if row == 2:
                    stri += "|_|"
                if row == 3:
                    stri += "..|"
                if position < len(str(n)):
                    stri += " "
                    position += 1
            if j == "5":
                if row == 1:
                    stri += "._."
                if row == 2:
                    stri += "|_."
                if row == 3:
                    stri += "._|"
                if position < len(str(n)):
                    stri += " "
                    position += 1
            if j == "6":
                if row == 1:
                    stri += "._."
                if row == 2:
                    stri += "|_."
                if row == 3:
                    stri += "|_|"
                if position < len(str(n)):
                    stri += " "
                    position += 1
            if j == "7":
                if row == 1:
                    stri += "._."
                if row == 2:
                    stri += "..|"
                if row == 3:
                    stri += "..|"
                if position < len(str(n)):
                    stri += " "
                    position += 1
            if j == "8":
                if row == 1:
                    stri += "._."
                if row == 2:
                    stri += "|_|"
                if row == 3:
                    stri += "|_|"
                if position < len(str(n)):
                    stri += " "
                    position += 1
            if j == "9":
                if row == 1:
                    stri += "._."
                if row == 2:
                    stri += "|_|"
                if row == 3:
                    stri += "..|"
                if position < len(str(n)):
                    stri += " "
                    position += 1
        position = 1
        row += 1
        if i < 2:
            stri += "\n"

    return stri


@app.route("/lcd/<int:number>")
def html_formation(number):
    stri = drawer(number)
    stri = stri.replace("\n", "<br>")
    stri = stri.replace(".", "&nbsp")
    return stri


if __name__ == "__main__":
    app.run(port=8080)
