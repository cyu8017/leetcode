// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    let expr = '';
    for (const ch of s) if (!/\s/.test(ch)) expr += ch;
    let i = 0;
    const parse = () => {
        const stack = [];
        let num = 0;
        let sign = '+';
        while (i < expr.length) {
            const ch = expr[i];
            if (ch >= '0' && ch <= '9') num = num * 10 + (ch.charCodeAt(0) - 48);
            else if (ch === '(') {
                i++;
                num = parse();
            }
            if ((!(ch >= '0' && ch <= '9') && ch !== '(') || i === expr.length - 1) {
                if (ch === '+' || ch === '-' || ch === '*' || ch === '/' || ch === ')' || i === expr.length - 1) {
                    if (sign === '+') stack.push(num);
                    else if (sign === '-') stack.push(-num);
                    else if (sign === '*') stack[stack.length - 1] *= num;
                    else if (sign === '/') {
                        const top = stack.pop();
                        stack.push(Math.trunc(top / num));
                    }
                    if (ch === ')') {
                        let sum = 0;
                        for (const v of stack) sum += v;
                        return sum;
                    }
                    sign = ch;
                    num = 0;
                }
            }
            i++;
        }
        let total = 0;
        for (const v of stack) total += v;
        return total;
    };
    return parse();
};
