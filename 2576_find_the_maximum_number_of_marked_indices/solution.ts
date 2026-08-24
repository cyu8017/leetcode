// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

export function maxNumOfMarkedIndices(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    let i = 0, ans = 0;
    for (let j = Math.floor((n + 1) / 2); j < n; ++j) {
        if (2 * nums[i] <= nums[j]) {
            ans += 2;
            i++;
        }
    }
    return ans;
}
