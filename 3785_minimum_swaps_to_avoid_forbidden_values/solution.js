// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

var minSwaps = function(nums, forbidden) {
    const n = nums.length;
    const freq = new Map();
    for (const x of nums) freq.set(x, (freq.get(x) || 0) + 1);
    for (const x of forbidden) freq.set(x, (freq.get(x) || 0) + 1);
    for (const c of freq.values()) {
        if (c > n) return -1;
    }
    const bad = new Map();
    let total = 0, largest = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] === forbidden[i]) {
            bad.set(nums[i], (bad.get(nums[i]) || 0) + 1);
            total++;
            if (bad.get(nums[i]) > largest) largest = bad.get(nums[i]);
        }
    }
    if (Math.floor((total + 1) / 2) > largest) return Math.floor((total + 1) / 2);
    return largest;
};
