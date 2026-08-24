// LeetCode 2970 - Count the Number of Incremovable Subarrays I
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

export function incremovableSubarrayCount(nums: any): any {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            let prev = -1;
            let ok = true;
            for (let t = 0; t < n; t++) {
                if (t >= i && t <= j) continue;
                if (nums[t] <= prev) { ok = false; break; }
                prev = nums[t];
            }
            if (ok) ans++;
        }
    }
    return ans;
}
