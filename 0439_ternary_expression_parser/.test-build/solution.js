"use strict";
// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Solution = void 0;
class Solution {
    parseTernary(expression) {
        if (!expression.includes("?"))
            return expression;
        let separator = 2;
        let depth = 0;
        for (let index = 2; index < expression.length; index += 1) {
            if (expression[index] === "?")
                depth += 1;
            else if (expression[index] === ":") {
                if (depth === 0) {
                    separator = index;
                    break;
                }
                depth -= 1;
            }
        }
        if (expression[0] === "T") {
            return this.parseTernary(expression.slice(2, separator));
        }
        return this.parseTernary(expression.slice(separator + 1));
    }
}
exports.Solution = Solution;
