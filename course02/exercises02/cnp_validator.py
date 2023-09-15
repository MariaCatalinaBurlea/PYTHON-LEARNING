"""
A CNP is read from console (a no of 13 digits). VALID if ok, else INVALID
CNP is the form of S AA LL ZZ JJ NNN V

S - sex(M or F) and the century when the person was born
1/2 - 1 Jan 1900 - 31 Dec 1999
3/4 - 1 Jan 1800 - 31 Dec 1899
5/6 - 1 Jan 200 - 31 Dec 2099
7/8 - foreign people living in Romania
9 - foreign people

AA - 2 digit number represents the last 2 digits of the year of birth
eg: 1970 & male => 170

LL - 2 digit number repr the month of birth

ZZ - 2 digit number repr the birthday, for days [1, 9] 0 will be added

JJ - 2 digit number repr the county
Buzau - 10, Bucharest - [41, 46] -> the district(sector)

NNN - 3 digit number 001-999 -> county, population record office

C - check digit based on CNP
C = Sum( digit of CNP * the digit on the same position on 279146358279)/ 11
if remainder == 10
    C = 1
else C = remainder
"""""
import sys
from datetime import datetime

# The Romanian counties
_COUNTIES = {
    '01': 'Alba',
    '02': 'Arad',
    '03': 'Arges',
    '04': 'Bacau',
    '05': 'Bihor',
    '06': 'Bistrita-Nasaud',
    '07': 'Botosani',
    '08': 'Brasov',
    '09': 'Braila',
    '10': 'Buzau',
    '11': 'Caras-Severin',
    '12': 'Cluj',
    '13': 'Constanta',
    '14': 'Covasna',
    '15': 'Dambovita',
    '16': 'Dolj',
    '17': 'Galati',
    '18': 'Gorj',
    '19': 'Harghita',
    '20': 'Hunedoara',
    '21': 'Ialomita',
    '22': 'Iasi',
    '23': 'Ilfov',
    '24': 'Maramures',
    '25': 'Mehedinti',
    '26': 'Mures',
    '27': 'Neamt',
    '28': 'Olt',
    '29': 'Prahova',
    '30': 'Satu Mare',
    '31': 'Salaj',
    '32': 'Sibiu',
    '33': 'Suceava',
    '34': 'Teleorman',
    '35': 'Timis',
    '36': 'Tulcea',
    '37': 'Vaslui',
    '38': 'Valcea',
    '39': 'Vrancea',
    '40': 'Bucuresti',
    '41': 'Bucuresti - Sector 1',
    '42': 'Bucuresti - Sector 2',
    '43': 'Bucuresti - Sector 3',
    '44': 'Bucuresti - Sector 4',
    '45': 'Bucuresti - Sector 5',
    '46': 'Bucuresti - Sector 6',
    '47': 'Bucuresti - Sector 7 (desfiintat)',
    '48': 'Bucuresti - Sector 8 (desfiintat)',
    '51': 'Calarasi',
    '52': 'Giurgiu',
}

_CHECK_NUMBER = "279146358279"


def get_birth_year_interval(given_cnp):
    digit = int(given_cnp[0])
    if digit in {1, 2, 7, 8, 9}:
        return 1900, 1999
    elif digit in {3, 4}:
        return 1800, 1899
    elif digit in {5, 6}:
        return 2000, 2099

    # match digit:
    #     case 1:
    #     case 2:
    #     case 7:
    #     case 8:
    #     case 9:
    #         return 1900, 1999
    #     case 3:
    #     case 4:
    #         return 1800, 1899
    #     case 5:
    #         case
    #         6:
    #         return 2000, 2099


def get_sex(given_cnp):
    if int(given_cnp[0]) % 2:
        return 'M'
    return 'F'


def get_birth_year(given_cnp):
    first_digit_aa = int(given_cnp[1])
    second_digit_aa = int(given_cnp[2])
    aa = int(first_digit_aa * 10 + second_digit_aa)
    [start_year, _] = get_birth_year_interval(given_cnp)
    return int(start_year/100 * 100 + aa)


def get_birth_month(given_cnp):
    first_digit_ll = int(given_cnp[3])
    second_digit_ll = int(given_cnp[4])
    return int(first_digit_ll * 10 + second_digit_ll)


def is_valid_month(given_cnp):
    month = get_birth_month(given_cnp)
    return 0 < month <= 12


def get_birth_day(given_cnp):
    first_digit_zz = int(given_cnp[5])
    second_digit_zz = int(given_cnp[6])
    return first_digit_zz * 10 + second_digit_zz


def get_birth_date(given_cnp):
    """Split the date parts from the number and return the birthdate."""
    centuries = {
        '1': 1900, '2': 1900, '3': 1800, '4': 1800, '5': 2000, '6': 2000,
    }  # we assume 1900 for the others in order to try to construct a date
    year = int(given_cnp[1:3]) + centuries.get(given_cnp[0], 1900)
    month = int(given_cnp[3:5])
    day = int(given_cnp[5:7])
    try:
        formatted_date = f"{year}-{month:02d}-{day:02d}"
        datetime.strptime(formatted_date, "%Y-%m-%d")
        print("Birth date: ", formatted_date)
    except ValueError:
        print("INVALID")
        sys.exit()
    except Exception:
        print("INVALID")
        sys.exit()


def is_valid_day(given_cnp):
    day = get_birth_day(given_cnp)
    return 1 <= day <= 31


def get_county(given_cnp):
    return _COUNTIES[given_cnp[7:9]]


def is_valid_county(given_cnp):
    try:
        print("County: ", get_county(given_cnp))
    except KeyError:
        print("INVALID")
        sys.exit()
    except Exception:
        print("INVALID")
        sys.exit()


def get_nnn(given_cnp):
    return given_cnp[9: 12]


def is_valid_nnn(given_cnp):
    nnn = get_nnn(given_cnp)
    nnn_int = int(nnn)
    if 1 <= nnn_int <= 999:
        print("NNN: ", nnn)
        return
    print("INVALID")
    sys.exit()


def compute_check_digit(given_cnp):
    sum_of_digits = 0
    cnp_without_check_digit = given_cnp[:-1]
    for index, digit in enumerate(cnp_without_check_digit):
        sum_of_digits += int(digit) * int(_CHECK_NUMBER[index])
    remainder = sum_of_digits % 11
    if remainder == 0:
        return 10
    return remainder


def is_valid_check_digit(given_cnp):
    check_digit = int(given_cnp[-1])
    expected_check_digit = compute_check_digit(given_cnp)
    if check_digit != expected_check_digit:
        print("INVALID")
        sys.exit()
    else:
        print(f"Check digit: {check_digit}")


cnp = input("Enter a cnp: ")
cnp_list = list(cnp)

# S - sex + century
print("Sex: ", get_sex(cnp))
print("Century interval", get_birth_year_interval(cnp))

# AA - birth year
birth_year = get_birth_year(cnp)
print("Birth year: ", birth_year)

# LL - month year
birth_month = get_birth_month(cnp)
print("Birth month: ", birth_month)
if not is_valid_month(cnp):
    print("INVALID")
    sys.exit()

# ZZ - birthday
birth_day = get_birth_day(cnp)
print("Birth day: ", birth_day)
if not is_valid_day(cnp):
    print("INVALID")
    sys.exit()

# get birthdate
get_birth_date(cnp)

# get county
is_valid_county(cnp)

# get nnn
is_valid_nnn(cnp)

# get check digit
is_valid_check_digit(cnp)

print("VALID")
