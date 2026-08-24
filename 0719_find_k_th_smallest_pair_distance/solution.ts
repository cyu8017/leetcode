// LeetCode 0719 - Find K-th Smallest Pair Distance
// https://leetcode.com/problems/find-k-th-smallest-pair-distance/

export function smallestDistancePair(nums: number[], k: number): number {
    nums = nums.slice().sort((a, b) => a - b);
    const countPairs = (distance) => {
        let count = 0, left = 0;
        for (let right = 0; right < nums.length; right++) {
            while (nums[right] - nums[left] > distance) left++;
            count += right - left;
        }
        return count;
    };
    let lo = 0, hi = nums[nums.length - 1] - nums[0];
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (countPairs(mid) >= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
