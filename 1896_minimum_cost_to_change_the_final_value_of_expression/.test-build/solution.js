"use strict";
// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/
function minOperationsToFlip(expression) {
    const combine = (left, op, right) => {
        const [leftVal, leftToZero, leftToOne] = left;
        const [rightVal, rightToZero, rightToOne] = right;
        let val = 0, toZero = 0, toOne = 0;
        if (op === "&") {
            const andVal = leftVal & rightVal;
            const andToZero = Math.min(leftToZero, leftToOne + rightToZero);
            const andToOne = leftToOne + rightToOne;
            const orToZero = leftToZero + rightToZero;
            const orToOne = Math.min(leftToOne, leftToZero + rightToOne, rightToZero + leftToOne);
            val = andVal;
            toZero = Math.min(andToZero, 1 + orToZero);
            toOne = Math.min(andToOne, 1 + orToOne);
        }
        else {
            const orVal = leftVal | rightVal;
            const orToZero = leftToZero + rightToZero;
            const orToOne = Math.min(leftToOne, leftToZero + rightToOne, rightToZero + leftToOne);
            const andToZero = Math.min(leftToZero, leftToOne + rightToZero);
            const andToOne = leftToOne + rightToOne;
            val = orVal;
            toZero = Math.min(orToZero, 1 + andToZero);
            toOne = Math.min(orToOne, 1 + andToOne);
        }
        return [val, toZero, toOne];
    };
    let index = 0;
    const parseFactor = () => {
        if (expression[index] === "0" || expression[index] === "1") {
            const value = Number(expression[index++]);
            return [value, value === 0 ? 0 : 1, value === 0 ? 1 : 0];
        }
        index++;
        const node = parseExpr();
        index++;
        return node;
    };
    const parseExpr = () => {
        let node = parseFactor();
        while (index < expression.length && (expression[index] === "&" || expression[index] === "|")) {
            const op = expression[index++];
            node = combine(node, op, parseFactor());
        }
        return node;
    };
    const [value, toZero, toOne] = parseExpr();
    return value ? toZero : toOne;
}
