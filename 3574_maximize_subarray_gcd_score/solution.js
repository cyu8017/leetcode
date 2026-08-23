// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

function gcd3574(a, b) {
    while (b !== 0) { const t = a % b; a = b; b = t; }
    return a;
}
var maxGCDScore = function(nums, k) {
    const n = nums.length;
    const cnt = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        let x = nums[i];
        while (x % 2 === 0) { cnt[i]++; x = Math.floor(x / 2); }
    }
    let ans = 0;
    for (let l = 0; l < n; l++) {
        let g = 0, mi = 2147483647, t = 0;
        for (let r = l; r < n; r++) {
            g = gcd3574(g, nums[r]);
            if (cnt[r] < mi) { mi = cnt[r]; t = 1; }
            else if (cnt[r] === mi) t++;
            let score = g * (r - l + 1);
            if (t <= k) score *= 2;
            ans = Math.max(ans, score);
        }
    }
    return ans;
};
