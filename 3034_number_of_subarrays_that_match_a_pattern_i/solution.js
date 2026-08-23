// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

function fRel(a, b) {
    if (a === b) return 0;
    return a < b ? 1 : -1;
}
var countMatchingSubarrays = function(nums, pattern) {
    const n = nums.length, m = pattern.length;
    let ans = 0;
    for (let i = 0; i < n - m; i++) {
        let ok = 1;
        for (let k = 0; k < m && ok !== 0; k++)
            if (fRel(nums[i + k], nums[i + k + 1]) !== pattern[k]) ok = 0;
        ans += ok;
    }
    return ans;
};
