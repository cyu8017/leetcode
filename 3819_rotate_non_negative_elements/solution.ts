// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate_non_negative_elements/

export function rotateElements(nums: any, k: any): any {
    const t = [];
    for (const x of nums) if (x >= 0) t.push(x);
    const m = t.length;
    if (m === 0) return nums;
    const d = new Array(m);
    for (let i = 0; i < m; i++) d[((i - k) % m + m) % m] = t[i];
    let j = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] >= 0) nums[i] = d[j++];
    }
    return nums;
}
