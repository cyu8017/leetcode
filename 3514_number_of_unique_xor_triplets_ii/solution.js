// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

var uniqueXorTriplets = function(nums) {
    let mx = 0;
    for (const v of nums) mx = Math.max(mx, v);
    mx <<= 1;
    const st = new Array(mx).fill(false);
    for (const a of nums) for (const b of nums) st[a ^ b] = true;
    const s = new Array(mx).fill(0);
    for (let ab = 0; ab < mx; ab++) {
        if (st[ab]) for (const c of nums) s[ab ^ c] = 1;
    }
    let ans = 0;
    for (const v of s) ans += v;
    return ans;
};
