// LeetCode 3728 - Stable Subarrays With Equal Boundary And Interior Sum
// https://leetcode.com/problems/stable_subarrays_with_equal_boundary_and_interior_sum/

var countStableSubarrays = function(capacity) {
    const n = capacity.length;
    const s = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) s[i] = s[i - 1] + capacity[i - 1];
    const cnt = new Map();
    let ans = 0;
    for (let r = 2; r < n; r++) {
        const l = r - 2;
        const keyL = capacity[l] + "#" + (capacity[l] + s[l + 1]);
        cnt.set(keyL, (cnt.get(keyL) || 0) + 1);
        const keyR = capacity[r] + "#" + s[r];
        ans += cnt.get(keyR) || 0;
    }
    return ans;
};
