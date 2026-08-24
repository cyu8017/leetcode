// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

let GOOD3890 = null;
function init3890(): any {
    if (GOOD3890) return;
    const LIMIT = 1000000000;
    const cnt = new Map();
    const cubes = new Array(1001);
    for (let i = 0; i <= 1000; i++) cubes[i] = i * i * i;
    for (let a = 1; a <= 1000; a++) {
        for (let b = a; b <= 1000; b++) {
            const x = cubes[a] + cubes[b];
            if (x > LIMIT) break;
            cnt.set(x, (cnt.get(x) || 0) + 1);
        }
    }
    GOOD3890 = [];
    for (const [k, v] of cnt.entries()) {
        if (v > 1) GOOD3890.push(k);
    }
    GOOD3890.sort((a, b) => a - b);
}export function findGoodIntegers(n: any): any {
    init3890();
    let lo = 0, hi = GOOD3890.length;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (GOOD3890[mid] <= n) lo = mid + 1;
        else hi = mid;
    }
    return GOOD3890.slice(0, lo);
}
