// LeetCode 2232 - Minimize Result by Adding Parentheses to Expression
// https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

/**
 * @param {string} expression
 * @return {string}
 */
var minimizeResult = function(expression) {
    const plus = expression.indexOf('+');
    const left = expression.slice(0, plus);
    const right = expression.slice(plus + 1);
    let bestVal = Infinity, best = '';
    for (let i = 0; i < left.length; i++) {
        for (let j = 1; j <= right.length; j++) {
            const a = left.slice(0, i);
            const b = left.slice(i);
            const c = right.slice(0, j);
            const d = right.slice(j);
            let val = parseInt(b, 10) + parseInt(c, 10);
            if (a.length) val *= parseInt(a, 10);
            if (d.length) val *= parseInt(d, 10);
            const cand = a + '(' + b + '+' + c + ')' + d;
            if (val < bestVal) { bestVal = val; best = cand; }
        }
    }
    return best;
};
