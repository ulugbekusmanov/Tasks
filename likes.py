arr = ["Ula"]


def likes(arr: list) -> str:
    if not arr:
        return "no one likes this"
    elif len(arr) == 1:
        return arr[0] + " likes this"
    elif len(arr) == 2:
        return arr[0] + " and " + arr[-1] + " like this"
    elif len(arr) == 3:
        return arr[0] + ", " + arr[1] + " and " + arr[-1] + " like this"
    else:
        return arr[0] + ", " + arr[1] + " and " + str(len(arr) - 2) + " others like this"
