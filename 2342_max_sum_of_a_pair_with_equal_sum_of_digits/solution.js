// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    const digitSum = (x) => {
        let s = 0;
        while (x > 0) { s += x % 10; x = Math.floor(x / 10); }
        return s;
    };
    const best = new Map();
    let ans = -1;
    for (const x of nums) {
        const ds = digitSum(x);
        if (best.has(ds)) {
            ans = Math.max(ans, best.get(ds) + x);
            if (x > best.get(ds)) best.set(ds, x);
        } else {
            best.set(ds, x);
        }
    }
    return ans;
};
