// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
// @ts-nocheck

function maxNonOverlapping(nums: number[], target: number): number {
    let seen = new Set([0]);
    let prefix = 0, answer = 0;
    for (const value of nums) {
        prefix += value;
        if (seen.has(prefix - target)) {
            answer++;
            prefix = 0;
            seen = new Set([0]);
        } else {
            seen.add(prefix);
        }
    }
    return answer;
}
