// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

export function numSubarrayBoundedMax(nums: number[], left: number, right: number): number {
    const countAtMost = (bound) => {
        let ans = 0, cur = 0;
        for (const num of nums) {
            if (num <= bound) {
                cur++;
                ans += cur;
            } else {
                cur = 0;
            }
        }
        return ans;
    };
    return countAtMost(right) - countAtMost(left - 1);
}
