// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

export function divideArray(nums: any, k: any): any {
    nums.sort((a, b) => a - b);
    const ans = [];
    for (let i = 0; i < nums.length; i += 3) {
        if (nums[i + 2] - nums[i] > k) return [];
        ans.push([nums[i], nums[i + 1], nums[i + 2]]);
    }
    return ans;
}
