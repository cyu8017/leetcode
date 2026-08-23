// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

function gcd(a, b) {
    while (b !== 0) {
        const t = a % b;
        a = b;
        b = t;
    }
    return a;
}
var countSequences = function(nums, k) {
    const f = new Map();
    const dfs = (i, p, q) => {
        if (i === nums.length) return (p === k && q === 1) ? 1 : 0;
        const key = i + ',' + p + ',' + q;
        if (f.has(key)) return f.get(key);
        let res = dfs(i + 1, p, q);
        const x = nums[i];
        const g1 = gcd(p * x, q);
        res += dfs(i + 1, (p * x) / g1, q / g1);
        const g2 = gcd(p, q * x);
        res += dfs(i + 1, p / g2, (q * x) / g2);
        f.set(key, res);
        return res;
    };
    return dfs(0, 1, 1);
};
