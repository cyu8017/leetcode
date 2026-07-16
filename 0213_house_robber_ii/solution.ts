// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

export function rob(nums: number[]): number {
    if (nums.length === 1) {
        return nums[0];
    }

    const robLinear = (houses: number[]): number => {
        let prev2 = 0;
        let prev1 = 0;
        for (const num of houses) {
            [prev2, prev1] = [prev1, Math.max(prev1, prev2 + num)];
        }
        return prev1;
    };

    return Math.max(robLinear(nums.slice(0, -1)), robLinear(nums.slice(1)));
}
