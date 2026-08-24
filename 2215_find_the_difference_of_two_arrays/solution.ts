// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

export function findDifference(nums1: number[], nums2: number[]): number[][] {
    const s1 = new Set(nums1), s2 = new Set(nums2);
    const a = [], b = [];
    for (const x of s1) if (!s2.has(x)) a.push(x);
    for (const x of s2) if (!s1.has(x)) b.push(x);
    return [a, b];
}
