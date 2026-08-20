// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

function kthLargestNumber(nums: string[], k: number): string {
    return nums.slice().sort((a, b: any) => (a.length !== b.length ? b.length - a.length : b.localeCompare(a)))[k - 1];
}
