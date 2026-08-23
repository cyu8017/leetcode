// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

var popcountDepth = function(nums, queries) {
    const bitCount = (x) => {
        let c = 0n, v = BigInt(x);
        while (v) { c += v & 1n; v >>= 1n; }
        return Number(c);
    };
    const depth = (x) => {
        let v = typeof x === 'bigint' ? x : BigInt(x);
        if (v === 1n) return 0;
        let d = 0;
        while (v > 1n) {
            v = BigInt(bitCount(v));
            d++;
        }
        return d;
    };
    const a = nums.slice();
    const ans = [];
    for (const q of queries) {
        if (q[0] === 1) {
            const l = Number(q[1]), r = Number(q[2]), k = Number(q[3]);
            let cnt = 0;
            for (let i = l; i <= r; i++)
                if (depth(a[i]) === k) cnt++;
            ans.push(cnt);
        } else {
            a[Number(q[1])] = q[2];
        }
    }
    return ans;
};
