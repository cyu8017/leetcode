// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

/**
 * @param {string} expression
 * @return {string[]}
 */
var braceExpansionII = function(expression) {
    function parse(expr, i) {
        const union = new Set();
        let cur = new Set([""]);
        while (i < expr.length && expr[i] !== "}") {
            if (expr[i] === "{") {
                const [nested, nextI] = parse(expr, i + 1);
                const next = new Set();
                for (const a of cur) {
                    for (const b of nested) next.add(a + b);
                }
                cur = next;
                i = nextI;
            } else if (expr[i] === ",") {
                for (const x of cur) union.add(x);
                cur = new Set([""]);
                i++;
            } else {
                let j = i;
                while (j < expr.length && /[a-z]/.test(expr[j])) j++;
                const token = expr.slice(i, j);
                const next = new Set();
                for (const a of cur) next.add(a + token);
                cur = next;
                i = j;
            }
        }
        for (const x of cur) union.add(x);
        return [union, i + 1];
    }
    const [result] = parse(expression, 0);
    return [...result].sort();
};
