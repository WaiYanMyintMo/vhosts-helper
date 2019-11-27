# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Replace function
def theme(template_local: str, keyword_config_local: dict) -> str:
    for keyword in keyword_config_local.keys():
        config = keyword_config_local[keyword]
        template_local = template_local.replace(keyword, config)
    return template_local


# Template Keywords
# Keywords to custom
# Template, and replace
# Return Replaced


if __name__ == "__main__":
    # Replace SvrName with Example1.com and Dir1 with D:/Example1
    keyword_config = {'SvrName': 'Example1.com',
                      'Dir1': r'D:\Example1'}
    # We got the template string and it is "i love my SvrName located in Dir1 Directory"
    template = "i love my SvrName located in Dir1 Directory"
    output = theme(template, keyword_config)

    # Test Case
    expected = r"i love my Example1.com located in D:\Example1 Directory"
    if output == expected:
        print('You did it, you crazy son of a bitch')
    else:
        print('What is wrong with you')