// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfSubarrays = function(nums) {
    const stk = [];
    let ans = 0;
    for (const x of nums) {
        while (stk.length && stk[stk.length - 1][0] < x) stk.pop();
        if (!stk.length || stk[stk.length - 1][0] > x) stk.push([x, 1]);
        else stk[stk.length - 1][1]++;
        ans += stk[stk.length - 1][1];
    }
    return ans;
};
