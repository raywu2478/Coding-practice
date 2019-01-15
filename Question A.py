def inputGuard(prompt):
    while True:
        try:
            num = float(input(prompt))
        except ValueError:
            print("Not a number")
            continue
        else:
            break

    return num


def overlap(a, b, c, d):
    if max(a, b) > min(c, d):
        print("Overlap")
    else:
        print("No overlap")


a = inputGuard("Enter x1: ")
b = inputGuard("Enter x2: ")
c = inputGuard("Enter x3: ")
d = inputGuard("Enter x4: ")

if min(a, b) < min(c, d):
    overlap(a, b, c, d)
else:
    overlap(c, d, a, b)
