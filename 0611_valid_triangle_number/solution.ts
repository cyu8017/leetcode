// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/

export function triangleNumber(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    let count = 0;
    for (let k = n - 1; k >= 2; --k) {
        let left = 0, right = k - 1;
        while (left < right) {
            if (nums[left] + nums[right] > nums[k]) {
                count += right - left;
                --right;
            } else {
                ++left;
            }
        }
    }
    return count;
}
