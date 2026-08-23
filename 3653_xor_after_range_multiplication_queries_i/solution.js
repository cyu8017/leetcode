// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

var xorAfterQueries = function(nums, queries) {
    const mod = 1000000007;
    for (const q of queries) {
        const l = q[0], r = q[1], k = q[2], v = q[3];
        for (let idx = l; idx <= r; idx += k)
            nums[idx] = Number(BigInt(nums[idx]) * BigInt(v) % BigInt(mod));
    }
    let ans = 0;
    for (const x of nums) ans ^= x;
    return ans;
};
