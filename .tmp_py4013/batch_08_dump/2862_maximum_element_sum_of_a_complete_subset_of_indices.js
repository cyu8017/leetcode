// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    const squareFree = (x) => {
        let res = 1;
        for (let p = 2; p * p <= x; p++) {
            let cnt = 0;
            while (x % p === 0) { x = Math.floor(x / p); cnt++; }
            if (cnt % 2 === 1) res *= p;
        }
        if (x > 1) res *= x;
        return res;
    };
    const n = nums.length;
    const groups = new Map();
    let ans = 0;
    for (let i = 1; i <= n; i++) {
        const sf = squareFree(i);
        const sum = (groups.get(sf) || 0) + nums[i - 1];
        groups.set(sf, sum);
        if (sum > ans) ans = sum;
    }
    return ans;
};
