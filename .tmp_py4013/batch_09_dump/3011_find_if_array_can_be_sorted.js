// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

function Popcount(x) {
    let c = 0;
    while (x !== 0) { c += x & 1; x >>= 1; }
    return c;
}
var canSortArray = function(nums) {
    let preMx = 0;
    let i = 0;
    const n = nums.length;
    while (i < n) {
        const cnt = Popcount(nums[i]);
        let j = i + 1;
        let mi = nums[i], mx = nums[i];
        while (j < n && Popcount(nums[j]) === cnt) {
            mi = Math.min(mi, nums[j]);
            mx = Math.max(mx, nums[j]);
            j++;
        }
        if (preMx > mi) return false;
        preMx = mx;
        i = j;
    }
    return true;
};
