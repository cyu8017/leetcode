// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

/**
 * @param {string} formula
 * @return {string}
 */
var countOfAtoms = function(formula) {
    const st = [new Map()];
    let i = 0;
    const n = formula.length;
    while (i < n) {
        if (formula[i] === '(') {
            st.push(new Map());
            i++;
        } else if (formula[i] === ')') {
            i++;
            const start = i;
            while (i < n && formula[i] >= '0' && formula[i] <= '9') i++;
            const mult = start < i ? parseInt(formula.substring(start, i), 10) : 1;
            const top = st.pop();
            const peek = st[st.length - 1];
            for (const [key, value] of top) {
                peek.set(key, (peek.get(key) || 0) + value * mult);
            }
        } else {
            let start = i++;
            while (i < n && formula[i] >= 'a' && formula[i] <= 'z') i++;
            const atom = formula.substring(start, i);
            start = i;
            while (i < n && formula[i] >= '0' && formula[i] <= '9') i++;
            const count = start < i ? parseInt(formula.substring(start, i), 10) : 1;
            const peek = st[st.length - 1];
            peek.set(atom, (peek.get(atom) || 0) + count);
        }
    }
    const peek = st[st.length - 1];
    const keys = Array.from(peek.keys()).sort();
    let result = '';
    for (const key of keys) {
        result += key;
        if (peek.get(key) > 1) result += peek.get(key);
    }
    return result;
};
