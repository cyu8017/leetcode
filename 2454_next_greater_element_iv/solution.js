// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var secondGreaterElement = function(nums) {
    const n = nums.length;
    const ans = Array(n).fill(-1);
    const stack1 = [], stack2 = [];
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        while (stack2.length && nums[stack2[stack2.length - 1]] < x) {
            ans[stack2.pop()] = x;
        }
        const tmp = [];
        while (stack1.length && nums[stack1[stack1.length - 1]] < x) {
            tmp.push(stack1.pop());
        }
        for (let j = tmp.length - 1; j >= 0; j--) stack2.push(tmp[j]);
        stack1.push(i);
    }
    return ans;
};
