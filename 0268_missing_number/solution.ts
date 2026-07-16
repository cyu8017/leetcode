// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

function missingNumber(nums: number[]): number {
    const length = nums.length;
    const expected = (length * (length + 1)) / 2;
    let total = 0;
    for (const num of nums) {
        total += num;
    }
    return expected - total;
}
