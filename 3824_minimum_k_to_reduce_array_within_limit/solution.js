// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum_k_to_reduce_array_within_limit/

function check(nums, k) {
    let t = 0;
    for (const x of nums) t += Math.floor((x + k - 1) / k);
    return t <= k * k;
}
var minimumK = function(nums) {
    let lo = 1, hi = 100000;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (check(nums, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
