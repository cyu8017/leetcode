// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

function costRange(nums, pref, l, r) {
    const mid = (l + r) >> 1;
    const left = nums[mid] * (mid - l) - (pref[mid] - pref[l]);
    const right = (pref[r + 1] - pref[mid + 1]) - nums[mid] * (r - mid);
    return left + right;
}
var maxFrequencyScore = function(nums, k) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    let ans = 1, left = 0;
    for (let right = 0; right < n; right++) {
        while (costRange(nums, pref, left, right) > k) left++;
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
};
