// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

export function distinctAverages(nums: number[]): number {
    nums = nums.slice().sort((a, b) => a - b);
    const seen = new Set();
    let l = 0, r = nums.length - 1;
    while (l < r) {
        seen.add(nums[l] + nums[r]);
        l++;
        r--;
    }
    return seen.size;
}
