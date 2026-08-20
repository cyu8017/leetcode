// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

function parseBoolExpr(expression: string): boolean {
    const stack = [];
    for (const ch of expression) {
        if (ch === ")") {
            const values = [];
            while (stack.length && !"&|!".includes(stack[stack.length - 1])) {
                const token = stack.pop();
                if (token === "t" || token === "f") values.push(token === "t");
            }
            const op = stack.pop();
            if (op === "!") {
                stack.push(values[0] ? "f" : "t");
            } else if (op === "&") {
                stack.push(values.every(Boolean) ? "t" : "f");
            } else {
                stack.push(values.some(Boolean) ? "t" : "f");
            }
        } else if (ch !== ",") {
            stack.push(ch);
        }
    }
    return stack[stack.length - 1] === "t";
}
