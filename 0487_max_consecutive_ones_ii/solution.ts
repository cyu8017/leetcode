// LeetCode 0487 - Max Consecutive Ones II
// https://leetcode.com/problems/max-consecutive-ones-ii/

export class Solution {
    findMaxConsecutiveOnes(nums: number[]): number {
        let left = 0;
        let best = 0;
        let zeros = 0;
        for (let right = 0; right < nums.length; right += 1) {
            if (nums[right] === 0) zeros += 1;
            while (zeros > 1) {
                if (nums[left] === 0) zeros -= 1;
                left += 1;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
