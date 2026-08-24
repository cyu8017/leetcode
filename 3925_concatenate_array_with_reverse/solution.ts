// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/

export function concatWithReverse(nums: any): any {
        let n = nums.length;
        let ans = new Array(2 * n).fill(0);
        for (let i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[n - i - 1];
        }
        return ans;
    
}
