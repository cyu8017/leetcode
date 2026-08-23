// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

var minChanges = function(nums, k) {
    const d = new Array(k + 2).fill(0);
    const n = nums.length;
    for (let i = 0; i < n / 2; i++) {
        let x = nums[i], y = nums[n - 1 - i];
        if (x > y) { const t = x; x = y; y = t; }
        d[0] += 1;
        d[y - x] -= 1;
        d[y - x + 1] += 1;
        const mx = Math.max(y, k - x);
        d[mx + 1] -= 1;
        d[mx + 1] += 2;
    }
    let ans = n, s = 0;
    for (const x of d) {
        s += x;
        ans = Math.min(ans, s);
    }
    return ans;
};
