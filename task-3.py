def check_brackets(string: str) -> str:
    stack = []
    brackets = {"(": ")", "[": "]", "{": "}"}
    opening_brackets = set(brackets.keys())
    closing_brackets = set(brackets.values())

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets[stack.pop()] != char:
                return "🚫 Non-symmetric separators"

    if stack:
        return "🚫 Non-symmetric separators"

    return "✅ Symmetric separators"


if __name__ == "__main__":
    input_string_1 = "( ){[ 1 ]( 1 + 3 )( ){ }}"
    input_string_2 = "( 23 ( 2 - 3);"
    input_string_3 = "( 11 }"

    print(f"{check_brackets(input_string_1)} === {input_string_1}")
    print(f"{check_brackets(input_string_2)} === {input_string_2}")
    print(f"{check_brackets(input_string_3)} === {input_string_3}")
