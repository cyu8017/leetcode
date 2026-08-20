// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

function arraysIntersection(arr1: number[], arr2: number[], arr3: number[]): number[] {
    const s2 = new Set(arr2), s3 = new Set(arr3);
    return [...new Set(arr1)].filter((x) => s2.has(x) && s3.has(x)).sort((a, b) => a - b);
}
