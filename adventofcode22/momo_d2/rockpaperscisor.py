with open("momo_d2/input") as file:
    lines = [line.rstrip().split() for line in file]


score = 0
for l in lines:
    match l[0]:
        case 'A': 
            match l[1]:
                case 'X':score += 0 + 3
                case 'Y': score += 3 + 1
                case 'Z': score += 6 + 2
        case 'B':
                match l[1]:
                    case 'X':score += 0 + 1
                    case 'Y': score += 3 + 2
                    case 'Z': score += 6 + 3
        case 'C':
            match l[1]:
                    case 'X':score += 0 + 2
                    case 'Y': score += 3 + 3
                    case 'Z': score += 6 + 1

print(score)