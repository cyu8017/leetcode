// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

export function minIncrementForUnique(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] <= nums[i - 1]) {
            const need = nums[i - 1] + 1;
            ans += need - nums[i];
            nums[i] = need;
        }
    }
    return ans;
}
