// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

export class Solution {
    splitArray(nums: number[]): boolean {
        const n = nums.length;
        if (n < 7) return false;

        const prefix = [0];
        for (const value of nums) prefix.push(prefix[prefix.length - 1] + value);

        for (let j = 3; j < n - 3; j++) {
            const seen = new Set<number>();
            for (let i = 1; i < j - 1; i++) {
                const first = prefix[i] - prefix[0];
                const second = prefix[j] - prefix[i + 1];
                if (first === second) seen.add(first);
            }
            for (let k = j + 2; k < n - 1; k++) {
                const third = prefix[k] - prefix[j + 1];
                const fourth = prefix[n] - prefix[k + 1];
                if (third === fourth && seen.has(third)) return true;
            }
        }
        return false;
    }
}
