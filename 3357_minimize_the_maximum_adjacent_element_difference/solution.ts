// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

function ok(d: any, nums: any, n: any): any {
    let prev = -1;
    for (let i = 0; i < n; i++) {
        if (nums[i] !== -1) {
            if (prev !== -1 && Math.abs(nums[i] - prev) > d) return false;
            prev = nums[i];
            continue;
        }
        let j = i;
        while (j < n && nums[j] === -1) j++;
        const left = prev;
        const right = (j < n) ? nums[j] : -1;
        const gap = j - i;
        if (left === -1 && right === -1) return true;
        if (left === -1 || right === -1) {
            prev = -1;
            i = j - 1;
            continue;
        }
        if (Math.abs(left - right) > d * (gap + 1)) return false;
        prev = -1;
        i = j - 1;
    }
    return true;
}export function minDifference(nums: any): any {
    const n = nums.length;
    let lo = 0, hi = 1000000000;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok(mid, nums, n)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
