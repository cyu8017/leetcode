// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

var specialTriplets = function(nums) {
    const left = new Map(), right = new Map();
    for (const x of nums) right.set(x, (right.get(x) || 0) + 1);
    let ans = 0;
    const mod = 1000000007;
    for (const x of nums) {
        right.set(x, right.get(x) - 1);
        const lv = left.get(x * 2) || 0;
        const rv = right.get(x * 2) || 0;
        ans = (ans + lv * rv % mod) % mod;
        left.set(x, (left.get(x) || 0) + 1);
    }
    return ans;
};
