def resistance2NominalValueInPOhms(resstr, *, Round):
        nominal = float(resstr.strip(' pnuµmkMGOhs'))
        if(Round):
            match(resstr[-5]):
                case 'p':
                    return nominal
                case 'n':
                    return round(nominal * 10e3, -1)
                case 'u' | 'µ':
                    return round(nominal * 10e6, -4)
                case 'm':
                    return round(nominal * 10e9, -7)
                case 'k':
                    return round(nominal * 10e15, -13)
                case 'M':
                    return round(nominal * 10e18, -16)
                case 'G':
                    return round(nominal * 10e21, -19)
                case " ":
                    return round(nominal * 10e12, 10)
                case _:
                    return 'Error!'
        else:
            match(resstr[-5]):
                case 'p':
                    return nominal
                case 'n':
                    return nominal * 10e3
                case 'u' | 'µ':
                    return nominal * 10e6
                case 'm':
                    return nominal * 10e9
                case 'k':
                    return nominal * 10e15
                case 'M':
                    return nominal * 10e18
                case 'G':
                    return nominal * 10e21
                case ' ':
                    return nominal * 10e12
                case _:
                    return "Error!"