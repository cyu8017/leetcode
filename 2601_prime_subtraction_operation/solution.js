// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var primeSubOperation = function(nums) {
    let maxV = 0;
    for (const x of nums) if (x > maxV) maxV = x;
    const isP = new Array(maxV + 1).fill(true);
    if (maxV >= 0) isP[0] = false;
    if (maxV >= 1) isP[1] = false;
    for (let i = 2; i * i <= maxV; ++i) {
        if (!isP[i]) continue;
        for (let j = i * i; j <= maxV; j += i) isP[j] = false;
    }
    const primes = [];
    for (let i = 2; i <= maxV; ++i) if (isP[i]) primes.push(i);
    let prev = 0;
    for (const x of nums) {
        const need = x - prev;
        let best = -1;
        for (const p of primes) {
            if (p >= need) break;
            best = p;
        }
        const cur = best < 0 ? x : x - best;
        if (cur <= prev) return false;
        prev = cur;
    }
    return true;
};
