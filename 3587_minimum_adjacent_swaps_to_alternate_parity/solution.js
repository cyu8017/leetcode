// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

function calc3587(pos, n, k) {
    let res = 0;
    for (let i = 0; i < n; i += 2) res += Math.abs(pos[k][Math.floor(i / 2)] - i);
    return res;
}
var minSwaps = function(nums) {
    const pos = [[], []];
    for (let i = 0; i < nums.length; i++) pos[nums[i] & 1].push(i);
    if (Math.abs(pos[0].length - pos[1].length) > 1) return -1;
    if (pos[0].length > pos[1].length) return calc3587(pos, nums.length, 0);
    if (pos[0].length < pos[1].length) return calc3587(pos, nums.length, 1);
    return Math.min(calc3587(pos, nums.length, 0), calc3587(pos, nums.length, 1));
};
