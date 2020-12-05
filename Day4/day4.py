from typing import Dict, Generator


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def read_passport_data() -> Generator[Dict[str, str], None, None]:
    passport_data: Dict[str, str] = {}
    for items in (line.split() for line in read_input()):
        if 0 == len(items):
            yield passport_data
            passport_data = {}

        for kv in [item.split(':') for item in items]:
            passport_data[kv[0]] = kv[1]

def is_valid_passport(items: Dict[str, str]) -> bool:
    return 'byr' in items.keys() \
        and 'iyr' in items.keys() \
        and 'eyr' in items.keys() \
        and 'hgt' in items.keys() \
        and 'hcl' in items.keys() \
        and 'ecl' in items.keys() \
        and 'pid' in items.keys()

def is_valid_birth_year(byr: str) -> bool:
    return byr.isnumeric() and 1920 <= int(byr) <= 2002

def is_valid_issue_year(iyr: str) -> bool:
    return iyr.isnumeric() and 2010 <= int(iyr) <= 2020

def is_valid_expiration_year(eyr: str) -> bool:
    return eyr.isnumeric() and 2020 <= int(eyr) <= 2030

def is_valid_height(hgt: str) -> bool:
    if len(hgt) < 3:
        return False

    unit = hgt[-2:]
    h = hgt[:-2]

    if 'cm' == unit:
        return h.isnumeric() and 150 <= int(h) <= 193

    if 'in' == unit:
        return h.isnumeric() and 59 <= int(h) <= 76

    return False

def is_valid_hair_color(hcl: str) -> bool:
    if len(hcl) != 7:
        return False
    
    if '#' != hcl[0]:
        return False
    
    rgb = hcl[1:]

    for c in rgb:
        if not (c.isnumeric() or c in ['a', 'b', 'c', 'd', 'e', 'f']):
            return False
    
    return True

def is_valid_eye_color(ecl: str) -> bool:
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_valid_passport_id(pid: str) -> bool:
    return 9 == len(pid) and pid.isnumeric()

def is_valid_passport_2(items: Dict[str, str]) -> bool:
    return is_valid_passport(items) \
        and is_valid_birth_year(items['byr']) \
        and is_valid_issue_year(items['iyr']) \
        and is_valid_expiration_year(items['eyr']) \
        and is_valid_height(items['hgt']) \
        and is_valid_hair_color(items['hcl']) \
        and is_valid_eye_color(items['ecl']) \
        and is_valid_passport_id(items['pid'])


if __name__ == '__main__':
    passports = [p for p in read_passport_data()]
    valid_passports = len([p for p in passports if is_valid_passport(p)])
    valid_passports_2 = len([p for p in passports if is_valid_passport_2(p)])

    print(f'Number of valid passports is {valid_passports}')
    print(f'Number of valid passports 2 is {valid_passports_2}')

