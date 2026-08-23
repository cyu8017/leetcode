// LeetCode 0394 - Decode String
var decodeString = function (s) {
    const stack = [];
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
            const [previous, count] = stack.pop();
            current = previous + current.repeat(count);
        } else {
            current += char;
        }
    }

    return current;
};

module.exports = { decodeString };
