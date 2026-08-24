// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

export function arrayNesting(nums: number[]): number {
    let best = 0;
    for (let i = 0; i < nums.length; ++i) {
        if (nums[i] < 0) continue;
        let length = 0;
        let j = i;
        while (nums[j] >= 0) {
            const nxt = nums[j];
            nums[j] = -1;
            j = nxt;
            ++length;
        }
        best = Math.max(best, length);
    }
    return best;
}
