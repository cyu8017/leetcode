// LeetCode 2557 - Maximum Number of Integers to Choose From a Range II
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/

/**
 * @param {number[]} banned
 * @param {number} n
 * @param {number} maxSum
 * @return {number}
 */
var maxCount = function(banned, n, maxSum) {
    banned.sort((a, b) => a - b);
    const uniq = [];
    for (const x of banned) {
        if (x >= 1 && x <= n && (!uniq.length || uniq[uniq.length - 1] !== x)) uniq.push(x);
    }
    let ans = 0, remain = maxSum, prev = 0;
    const check = (l, r) => {
        if (l > r || remain <= 0) return;
        let lo = l, hi = r, best = l - 1;
        while (lo <= hi) {
            const mid = Math.floor((lo + hi) / 2);
            const cnt = mid - l + 1;
            const sum = (l + mid) * cnt / 2;
            if (sum <= remain) {
                best = mid;
                lo = mid + 1;
            } else hi = mid - 1;
        }
        if (best >= l) {
            const cnt = best - l + 1;
            ans += cnt;
            remain -= (l + best) * cnt / 2;
        }
    };
    for (const b of uniq) {
        check(prev + 1, b - 1);
        prev = b;
    }
    check(prev + 1, n);
    return ans;
};
