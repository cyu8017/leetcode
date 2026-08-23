// LeetCode 3811 - Number Of Alternating Xor Partitions
// https://leetcode.com/problems/number_of_alternating_xor_partitions/

var alternatingXOR = function(nums, target1, target2) {
    const MOD = 1000000007;
    const cnt1 = new Map();
    const cnt2 = new Map();
    cnt2.set(0, 1);
    let pre = 0, ans = 0;
    for (const x of nums) {
        pre ^= x;
        const a = cnt2.get(pre ^ target1) || 0;
        const b = cnt1.get(pre ^ target2) || 0;
        ans = (a + b) % MOD;
        cnt1.set(pre, ((cnt1.get(pre) || 0) + a) % MOD);
        cnt2.set(pre, ((cnt2.get(pre) || 0) + b) % MOD);
    }
    return ans;
};
