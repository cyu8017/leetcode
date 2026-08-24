// LeetCode 3038 - Maximum Number of Operations With the Same Score I
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

export function maxOperations(nums: any): any {
    const s = nums[0] + nums[1];
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i + 1 < n && nums[i] + nums[i + 1] === s; i += 2) ans++;
    return ans;
}
