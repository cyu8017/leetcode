// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

export function countFairPairs(nums: number[], lower: number, upper: number): number {
    nums.sort((a, b) => a - b);
    const count = (x) => {
        let ans = 0, l = 0, r = nums.length - 1;
        while (l < r) {
            if (nums[l] + nums[r] <= x) {
                ans += r - l;
                l++;
            } else r--;
        }
        return ans;
    };
    return count(upper) - count(lower - 1);
}
