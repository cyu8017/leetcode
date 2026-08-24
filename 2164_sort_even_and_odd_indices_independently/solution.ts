// LeetCode 2164 - Sort Even and Odd Indices Independently
// https://leetcode.com/problems/sort-even-and-odd-indices-independently/

export function sortEvenOdd(nums: number[]): number[] {
    const even = [], odd = [];
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) even.push(nums[i]);
        else odd.push(nums[i]);
    }
    even.sort((a, b) => a - b);
    odd.sort((a, b) => b - a);
    let ei = 0, oi = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) nums[i] = even[ei++];
        else nums[i] = odd[oi++];
    }
    return nums;
}
