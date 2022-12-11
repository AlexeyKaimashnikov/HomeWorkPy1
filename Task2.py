def equality():
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]:
                if (not (x or y or z)) != (not (x) and not (y) and not (z)):
                    return('Выражение не выполняется')
                return ('Выражение всегда верно')
print(equality())
