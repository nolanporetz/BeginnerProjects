def bottle(n):
    if n == 0:
        return "No more bottles"
    elif n == 1:
        return str(n) + " more bottle"
    else:
        return str(n) + " bottles"


def lyrics(n=99):
    if n == 0:
        return bottle(n) + " of beer on the wall, " + bottle(n) + " of beer!\n" "Go to the store and buy some more, " + bottle(n) + " of beer on the wall!"
    else:
        return bottle(n) + " of beer on the wall, " + bottle(n) + " of beer!\n" "Take one down and pass it around, " + bottle(n-1) + " of beer on the wall!\n\n" + lyrics(n-1)

print(lyrics(99))

