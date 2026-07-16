// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    const stack = [];
    let result = 0;
    let number = 0;
    let sign = 1;
    for (const char of s) {
        if (char >= "0" && char <= "9") {
            number = number * 10 + (char.charCodeAt(0) - 48);
        } else if (char === "+" || char === "-") {
            result += sign * number;
            number = 0;
            sign = char === "+" ? 1 : -1;
        } else if (char === "(") {
            stack.push(result);
            stack.push(sign);
            result = 0;
            sign = 1;
        } else if (char === ")") {
            result += sign * number;
            number = 0;
            result *= stack.pop();
            result += stack.pop();
        }
    }
    result += sign * number;
    return result;
};
