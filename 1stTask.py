def calc_salt(weight):
    try:
        weight = int(weight)
    except:
        print(f'invalid literl for int() with base 10: {str(weight)}')
        print(0.0)
    else:
        result = weight / 100
        return result


print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))