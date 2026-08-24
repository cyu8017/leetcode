// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

function Gcd(a, b) {
    while (b !== 0) {
        const t = a % b;
        a = b;
        b = t;
    }
    return a;
}
var gcdSum = function(nums) {
    const n = nums.length;
    const prefixGcd = new Array(n);
    let mx = 0;
    for (let i = 0; i < n; i++) {
        mx = Math.max(mx, nums[i]);
        prefixGcd[i] = Gcd(nums[i], mx);
    }
    prefixGcd.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < Math.floor(n / 2); i++) ans += Gcd(prefixGcd[i], prefixGcd[n - i - 1]);
    return ans;
};
