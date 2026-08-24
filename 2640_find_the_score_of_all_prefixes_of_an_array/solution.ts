// LeetCode 2640 - Find the Score of All Prefixes of an Array
// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

export function findPrefixScore(nums: any): any {
    const ans = new Array(nums.length);
    let mx = 0, sum = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > mx) mx = nums[i];
        sum += nums[i] + mx;
        ans[i] = sum;
    }
    return ans;
}
