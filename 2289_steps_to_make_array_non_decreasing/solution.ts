// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

export function totalSteps(nums: any): any {
    const stack = [];
    let ans = 0;
    for (let i = nums.length - 1; i >= 0; i--) {
        let steps = 0;
        while (stack.length && nums[i] > stack[stack.length - 1][0]) {
            steps = Math.max(steps, stack[stack.length - 1][1]);
            stack.pop();
            steps++;
        }
        ans = Math.max(ans, steps);
        stack.push([nums[i], steps]);
    }
    return ans;
}
