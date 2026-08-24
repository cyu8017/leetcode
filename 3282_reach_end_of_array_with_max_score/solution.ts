// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

export function findMaximumScore(nums: any): any {
    let ans = 0, maxV = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > maxV) maxV = nums[i];
        ans += maxV;
    }
    return ans;
}
