// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate_valid_expressions/

var evaluateExpression = function(expression) {
    const parse = (i) => {
        const ch = expression[i];
        if ((ch >= '0' && ch <= '9') || ch === '-') {
            let j = i;
            if (expression[j] === '-') j++;
            while (j < expression.length && expression[j] >= '0' && expression[j] <= '9') j++;
            return [parseInt(expression.substring(i, j), 10), j];
        }
        let j = i;
        while (expression[j] !== '(') j++;
        const op = expression.substring(i, j);
        j++;
        const p1 = parse(j);
        j = p1[1] + 1;
        const p2 = parse(j);
        j = p2[1] + 1;
        let res = 0;
        if (op === "add") res = p1[0] + p2[0];
        else if (op === "sub") res = p1[0] - p2[0];
        else if (op === "mul") res = p1[0] * p2[0];
        else if (op === "div") res = Math.trunc(p1[0] / p2[0]);
        return [res, j];
    };
    return parse(0)[0];
};
