// LeetCode 3776 - Minimum Moves To Balance Circular Array
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

var minMoves = function(balance) {
    let sum = 0;
    for (const b of balance) sum += b;
    if (sum < 0) return -1;
    const n = balance.length;
    let mn = balance[0], idx = 0;
    for (let i = 1; i < n; i++) {
        if (balance[i] < mn) {
            mn = balance[i];
            idx = i;
        }
    }
    if (mn >= 0) return 0;
    let need = -mn;
    let ans = 0;
    for (let j = 1; j < n; j++) {
        const a = balance[(idx - j + n) % n];
        const b = balance[(idx + j) % n];
        const c1 = Math.min(a, need);
        need -= c1;
        ans += c1 * j;
        const c2 = Math.min(b, need);
        need -= c2;
        ans += c2 * j;
    }
    return ans;
};
