// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

function maxDistance(nums1: number[], nums2: number[]): number {
    let answer = 0, j = 0;
    for (let i = 0; i < nums1.length; i++) {
        while (j < nums2.length && nums1[i] <= nums2[j]) j++;
        answer = Math.max(answer, j - i - 1);
    }
    return answer;
}
