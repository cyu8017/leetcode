// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

export function numberGame(nums: any): any {
    nums.sort((a, b) => a - b);
    for (let i = 0; i + 1 < nums.length; i += 2) {
        const t = nums[i];
        nums[i] = nums[i + 1];
        nums[i + 1] = t;
    }
    return nums;
}
