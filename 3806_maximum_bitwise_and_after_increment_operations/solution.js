// LeetCode 3806 - Maximum Bitwise And After Increment Operations
// https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

var maximumAND = function(nums, k, m) {
    const BitLen = (x) => {
        if (x === 0) return 0;
        let n = 0;
        while (x > 0) { n++; x >>= 1; }
        return n;
    };
    let mxVal = nums[0];
    for (const v of nums) if (v > mxVal) mxVal = v;
    mxVal += k;
    const mx = BitLen(mxVal);
    let ans = 0;
    const cost = new Array(nums.length);
    for (let bit = mx - 1; bit >= 0; bit--) {
        const target = ans | (1 << bit);
        for (let i = 0; i < nums.length; i++) {
            const x = nums[i];
            const j = BitLen(target & ~x);
            const mask = (1 << j) - 1;
            cost[i] = (target & mask) - (x & mask);
        }
        cost.sort((a, b) => a - b);
        let sum = 0;
        for (let i = 0; i < m; i++) sum += cost[i];
        if (sum <= k) ans = target;
    }
    return ans;
};
