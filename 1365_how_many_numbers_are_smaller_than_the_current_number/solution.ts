// LeetCode 1365 - How Many Numbers Are Smaller Than The Current Number
// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

function smallerNumbersThanCurrent(nums: number[]): number[] {
    const sorted = [...nums].sort((a, b: any): any => a - b);
    return nums.map((x: any): any => sorted.indexOf(x));
}
