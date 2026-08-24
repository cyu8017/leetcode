// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

export function countGoodIntegers(l: any, r: any, k: any): any {
    return count(r, k) - count(l - 1, k);
}
function count(bound: any, k: any): any {
    if (bound <= 0) return 0;
    const digits = String(bound);
    const memo = new Map();
    return dfs(0, 0, false, true, digits, k, memo);
}
function dfs(position: any, previous: any, started: any, tight: any, digits: any, k: any, memo: any): any {
    if (position === digits.length) return started ? 1 : 0;
    const key = position + "," + previous + "," + started;
    if (!tight && memo.has(key)) return memo.get(key);
    const limit = tight ? digits.charCodeAt(position) - 48 : 9;
    let result = 0;
    for (let digit = 0; digit <= limit; digit++) {
        const nextStarted = started || digit !== 0;
        if (started && Math.abs(previous - digit) > k) continue;
        const nextPrevious = nextStarted ? digit : previous;
        result += dfs(position + 1, nextPrevious, nextStarted, tight && digit === limit, digits, k, memo);
    }
    if (!tight) memo.set(key, result);
    return result;
}
