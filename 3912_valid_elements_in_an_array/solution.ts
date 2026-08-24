// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

export function findValidElements(nums: any): any {
    const n = nums.length;
    const right = new Array(n);
    right[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) right[i] = Math.max(right[i + 1], nums[i]);
    let left = 0;
    const ans = [];
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        if (x > left || i === n - 1 || x > right[i + 1]) ans.push(x);
        left = Math.max(left, x);
    }
    return ans;
}
