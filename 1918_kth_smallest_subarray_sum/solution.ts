// LeetCode 1918 - Kth Smallest Subarray Sum
// https://leetcode.com/problems/kth-smallest-subarray-sum/

function kthSmallestSubarraySum(nums: number[], k: number): number {
    const count = (limit: any) => {
        let total = 0, left = 0, ans = 0;
        for (let right = 0; right < nums.length; right++) {
            total += nums[right];
            while (total > limit) total -= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    };
    let lo = Math.min(...nums), hi = nums.reduce((a, b: any) => a + b, 0);
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (count(mid) >= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
