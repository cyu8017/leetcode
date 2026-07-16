// LeetCode 0394 - Decode String
export function decodeString(s: string): string {
    const stack: [string, number][] = [];
    let current = "";
    let number = 0;

    for (const char of s) {
        if (char >= "0" && char <= "9") {
            number = number * 10 + Number(char);
        } else if (char === "[") {
            stack.push([current, number]);
            current = "";
            number = 0;
        } else if (char === "]") {
            const [previous, count] = stack.pop()!;
            current = previous + current.repeat(count);
        } else {
            current += char;
        }
    }

    return current;
}
