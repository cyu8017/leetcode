// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

export function calculate(s: string): number {
    const stack: number[] = [];
    let number = 0;
    let operator = "+";

    for (let index = 0; index < s.length; index += 1) {
        const char = s[index];
        if (char >= "0" && char <= "9") {
            number = number * 10 + (char.charCodeAt(0) - 48);
        }
        if (char === "+" || char === "-" || char === "*" || char === "/" || index === s.length - 1) {
            if (operator === "+") {
                stack.push(number);
            } else if (operator === "-") {
                stack.push(-number);
            } else if (operator === "*") {
                stack.push(stack.pop()! * number);
            } else if (operator === "/") {
                stack.push(Math.trunc(stack.pop()! / number));
            }
            operator = char;
            number = 0;
        }
    }

    return stack.reduce((sum, value) => sum + value, 0);
}
