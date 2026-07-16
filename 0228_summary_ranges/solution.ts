// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

export function summaryRanges(nums: number[]): string[] {
    const result: string[] = [];
    let index = 0;

    while (index < nums.length) {
        const start = nums[index];
        while (index + 1 < nums.length && nums[index + 1] === nums[index] + 1) {
            index += 1;
        }
        if (start === nums[index]) {
            result.push(String(start));
        } else {
            result.push(`${start}->${nums[index]}`);
        }
        index += 1;
    }

    return result;
}
