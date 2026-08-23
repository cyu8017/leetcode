// LeetCode 3431 - Minimum Unlocked Indices to Sort Nums
// https://leetcode.com/problems/minimum-unlocked-indices-to-sort-nums/

var minUnlockedIndices = function(nums, locked) {
    const n = nums.length;
    let need = false;
    for (let i = 1; i < n; i++) {
        if (nums[i] < nums[i - 1]) { need = true; break; }
    }
    if (!need) return 0;
    let left = n, right = -1;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (nums[i] > nums[j]) {
                if (i < left) left = i;
                if (j > right) right = j;
            }
        }
    }
    if (right < left) return 0;
    let ans = 0;
    for (let i = left; i <= right; i++) if (locked[i] === 1) ans++;
    const tmp = nums.slice();
    const lock = locked.slice();
    for (let i = left; i <= right; i++) lock[i] = 0;
    let changed = true;
    while (changed) {
        changed = false;
        for (let i = 0; i + 1 < n; i++) {
            if (lock[i] === 0 && lock[i + 1] === 0 && tmp[i] > tmp[i + 1]) {
                const t = tmp[i]; tmp[i] = tmp[i + 1]; tmp[i + 1] = t;
                changed = true;
            }
        }
    }
    for (let i = 1; i < n; i++) if (tmp[i] < tmp[i - 1]) return -1;
    return ans;
};
