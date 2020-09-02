def decorate_lower(word):
    def wrapper():
        lowerWord=word()
        newWord=lowerWord.lower()
        return newWord
    return wrapper

def decorate_upper(word):
    def wrapper():
        upperWord=word()
        newWord=upperWord.upper()
        return newWord
    return wrapper

def decorate_replace(word):
    def wrapper():
        replaceWord=word()
        newWord=replaceWord.replace("Saytin","Platformanin")
        return newWord
    return wrapper

def decorate_swapcase(word):
    def wrapper():
        swcase=word()
        newWord=swcase.swapcase()
        return newWord
    return wrapper

def decorate_plus(word):
    def wrapper():
        plus=word()
        new=f"{plus} elave olaraq da bir nece yazini uzerine gele bilerik"
        return new
    return wrapper

@decorate_lower
def home():
    return "SAYTIN BU HISSESINDE YERLESEN MENYULARIN HAMISI KICIK HERFLERLE YAZILACAQ"

@decorate_replace
def header():
    return "Saytin header hissesinin kodlari"

@decorate_upper
def footer():
    return "Saytin bu hissesindeki yazilar boyuk herflerle yazilacaq"

@decorate_swapcase
def section():
    return "BolMeler aRaSi yaziLar yeRLesdiriLeceK"

@decorate_plus
def test():
    return "Bu hissedeki yazilar mene aiddir"


print(home())
print(header())
print(section())
print(footer())
print(test())




# def decorate_plus(var):
#     def wrapper():
#         new=var()
#         newPlus=new+5
#         return newPlus
#     return wrapper
#
# def decorate_minus(var):
#     def wrapper():
#         new=var()
#         newMinus=new-5
#         return newMinus
#     return wrapper
#
#
# @decorate_plus
# def ededTopla():
#     return 22

# @decorate_minus
# def ededCix():
#     return 18
#
# print(ededTopla())
# print(ededCix())
