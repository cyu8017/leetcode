// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

function validSubarrays(nums: number[]): number {
    const stack: number[] = [];
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        while (stack.length && nums[stack[stack.length - 1]] > nums[i]) {
            const j = stack.pop()!;
            ans += i - j;
        }
        stack.push(i);
    }
    while (stack.length) {
        const j = stack.pop()!;
        ans += nums.length - j;
    }
    return ans;
}
