// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

/**
 * @param {string} expression
 * @return {string}
 */
var fractionAddition = function(expression) {
    const gcd = (a, b) => {
        a = Math.abs(a); b = Math.abs(b);
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    let numerator = 0, denominator = 1;
    let i = 0;
    const len = expression.length;
    while (i < len) {
        let sign = 1;
        if (expression[i] === "+" || expression[i] === "-") {
            if (expression[i] === "-") sign = -1;
            ++i;
        }
        let a = 0;
        while (i < len && expression[i] >= "0" && expression[i] <= "9") {
            a = a * 10 + (expression.charCodeAt(i) - 48);
            ++i;
        }
        a *= sign;
        ++i;
        let b = 0;
        while (i < len && expression[i] >= "0" && expression[i] <= "9") {
            b = b * 10 + (expression.charCodeAt(i) - 48);
            ++i;
        }
        numerator = numerator * b + a * denominator;
        denominator *= b;
        const g = gcd(numerator, denominator);
        numerator = Math.trunc(numerator / g);
        denominator = Math.trunc(denominator / g);
    }
    return numerator + "/" + denominator;
};
