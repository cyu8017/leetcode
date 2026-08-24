// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

var getLength = function(nums) {
    const n = nums.length;
    let ans = 1;
    for (let l = 0; l < n; l++) {
        const cnt = new Map();
        const freq = new Map();
        for (let r = l; r < n; r++) {
            const x = nums[r];
            const c = cnt.get(x) || 0;
            if ((freq.get(c) || 0) > 0) {
                const fc = freq.get(c) - 1;
                if (fc === 0) freq.delete(c);
                else freq.set(c, fc);
            }
            cnt.set(x, c + 1);
            freq.set(cnt.get(x), (freq.get(cnt.get(x)) || 0) + 1);
            const cx = cnt.get(x);
            if (cnt.size === 1 || (freq.size === 2 && ((freq.get(cx * 2) || 0) > 0 || (cx % 2 === 0 && (freq.get(cx / 2) || 0) > 0)))) {
                ans = Math.max(ans, r - l + 1);
            }
        }
    }
    return ans;
};
