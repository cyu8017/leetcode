// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

var minOperations = function(nums) {
    let f = new Map();
    f.set(nums[0], 0);
    for (let i = 1; i < nums.length; i++) {
        const x = nums[i];
        const g = new Map();
        for (const [pre, s] of f) {
            let cur = Math.ceil(x / pre) * pre;
            while (cur <= 100) {
                const val = s + (cur - x);
                const old = g.get(cur);
                if (old === undefined || old > val) g.set(cur, val);
                cur += pre;
            }
        }
        f = g;
    }
    let ans = Infinity;
    for (const v of f.values()) ans = Math.min(ans, v);
    return ans;
};
