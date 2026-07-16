// LeetCode 0537 - Complex Number Multiplication
// https://leetcode.com/problems/complex-number-multiplication/

class Solution {
    complexNumberMultiply(num1, num2) {
        const parse = (num) => {
            const [real, imagPart] = num.split("+");
            return [Number(real), Number(imagPart.slice(0, -1))];
        };

        const [a, b] = parse(num1);
        const [c, d] = parse(num2);
        const real = a * c - b * d;
        const imag = a * d + b * c;
        return `${real}+${imag}i`;
    }
}

module.exports = { Solution };
