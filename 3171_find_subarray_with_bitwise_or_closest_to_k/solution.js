// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

var minimumDifference = function(nums, k) {
    let mx = 0;
    for (const v of nums) mx = Math.max(mx, v);
    const m = mx === 0 ? 1 : 32 - leadingZeroCount(mx);
    const cnt = new Array(m).fill(0);
    let ans = Infinity, s = 0, i = 0;
    for (let j = 0; j < nums.length; j++) {
        const x = nums[j];
        s |= x;
        ans = Math.min(ans, Math.abs(s - k));
        for (let h = 0; h < m; h++) if (((x >> h) & 1) !== 0) cnt[h]++;
        while (i < j && s > k) {
            const y = nums[i];
            for (let h = 0; h < m; h++) {
                if (((y >> h) & 1) !== 0) {
                    if (--cnt[h] === 0) s ^= 1 << h;
                }
            }
            ans = Math.min(ans, Math.abs(s - k));
            i++;
        }
    }
    return ans;
};
function leadingZeroCount(x) {
    if (x === 0) return 32;
    let n = 0;
    for (let bit = 31; bit >= 0; bit--) {
        if (((x >> bit) & 1) !== 0) break;
        n++;
    }
    return n;
}
