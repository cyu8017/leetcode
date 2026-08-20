"use strict";
// LeetCode 1387: Sort Integers By The Power Value
function getKth(lo, hi, k) {
    const memo = new Map([[1, 0]]);
    const power = (value) => {
        if (!memo.has(value))
            memo.set(value, 1 + power(value % 2 ? 3 * value + 1 : value / 2));
        return memo.get(value);
    };
    return Array.from({ length: hi - lo + 1 }, (_, i) => lo + i).sort((a, b) => power(a) - power(b) || a - b)[k - 1];
}
