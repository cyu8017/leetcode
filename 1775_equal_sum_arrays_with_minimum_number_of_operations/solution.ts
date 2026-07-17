// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

function minOperations(nums1: number[], nums2: number[]): number {
    if (nums1.length * 6 < nums2.length || nums2.length * 6 < nums1.length) {
        return -1;
    }
    let s1 = nums1.reduce((a, b) => a + b, 0);
    let s2 = nums2.reduce((a, b) => a + b, 0);
    if (s1 === s2) {
        return 0;
    }
    if (s1 < s2) {
        [nums1, nums2] = [nums2, nums1];
        [s1, s2] = [s2, s1];
    }
    let diff = s1 - s2;
    const gains = [...nums1.map((x) => x - 1), ...nums2.map((x) => 6 - x)].sort(
        (a, b) => b - a,
    );
    let ops = 0;
    for (const gain of gains) {
        if (diff <= 0) {
            break;
        }
        diff -= gain;
        ops++;
    }
    return diff <= 0 ? ops : -1;
}
