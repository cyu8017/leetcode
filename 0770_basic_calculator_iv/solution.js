// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

/**
 * @param {string} expression
 * @param {string[]} evalvars
 * @param {number[]} evalints
 * @return {string[]}
 */
var basicCalculatorIV = function(expression, evalvars, evalints) {
    const values = new Map();
    for (let i = 0; i < evalvars.length; i++) values.set(evalvars[i], evalints[i]);
    const tokens = [];
    let cur = '';
    for (const ch of expression) {
        if (ch === '(' || ch === ')') {
            if (cur.length > 0) { tokens.push(cur); cur = ''; }
            tokens.push(ch);
        } else if (/\s/.test(ch)) {
            if (cur.length > 0) { tokens.push(cur); cur = ''; }
        } else cur += ch;
    }
    if (cur.length > 0) tokens.push(cur);
    let pos = 0;

    const keyOf = (items) => items.join('\0');
    const itemsOf = (key) => (key === '' ? [] : key.split('\0'));

    const clean = (poly) => {
        for (const [k, v] of [...poly.entries()]) if (v === 0) poly.delete(k);
        return poly;
    };

    const add = (left, right) => {
        const result = new Map(left);
        for (const [k, v] of right) result.set(k, (result.get(k) || 0) + v);
        return clean(result);
    };

    const negate = (poly) => {
        const result = new Map();
        for (const [k, v] of poly) result.set(k, -v);
        return result;
    };

    const mul = (left, right) => {
        const result = new Map();
        for (const [lk, lv] of left) {
            for (const [rk, rv] of right) {
                const keyList = itemsOf(lk).concat(itemsOf(rk)).sort();
                const key = keyOf(keyList);
                result.set(key, (result.get(key) || 0) + lv * rv);
            }
        }
        return clean(result);
    };

    const atom = (token) => {
        const poly = new Map();
        if (/[a-zA-Z]/.test(token[0])) {
            if (values.has(token)) poly.set('', values.get(token));
            else poly.set(keyOf([token]), 1);
        } else poly.set('', parseInt(token, 10));
        return clean(poly);
    };

    const parseFactor = () => {
        if (tokens[pos] === '(') {
            pos++;
            const poly = parseExpr();
            pos++;
            return poly;
        }
        return atom(tokens[pos++]);
    };

    const parseTerm = () => {
        let poly = parseFactor();
        while (pos < tokens.length && tokens[pos] === '*') {
            pos++;
            poly = mul(poly, parseFactor());
        }
        return poly;
    };

    const parseExpr = () => {
        let poly = parseTerm();
        while (pos < tokens.length && (tokens[pos] === '+' || tokens[pos] === '-')) {
            const op = tokens[pos++];
            const right = parseTerm();
            poly = add(poly, op === '+' ? right : negate(right));
        }
        return poly;
    };

    const compareLists = (a, b) => {
        const n = Math.min(a.length, b.length);
        for (let i = 0; i < n; i++) {
            if (a[i] < b[i]) return -1;
            if (a[i] > b[i]) return 1;
        }
        return a.length - b.length;
    };

    const poly = parseExpr();
    const keys = Array.from(poly.entries());
    keys.sort((a, b) => {
        const ai = itemsOf(a[0]), bi = itemsOf(b[0]);
        if (ai.length !== bi.length) return bi.length - ai.length;
        return compareLists(ai, bi);
    });
    const answer = [];
    for (const [k, v] of keys) {
        if (v === 0) continue;
        const items = itemsOf(k);
        if (items.length === 0) answer.push(String(v));
        else answer.push(String(v) + '*' + items.join('*'));
    }
    return answer;
};
