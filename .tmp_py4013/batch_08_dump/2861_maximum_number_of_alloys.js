// LeetCode 2861 - Maximum Number of Alloys
// https://leetcode.com/problems/maximum-number-of-alloys/

/**
 * @param {number} n
 * @param {number} k
 * @param {number} budget
 * @param {number[][]} composition
 * @param {number[]} stock
 * @param {number[]} cost
 * @return {number}
 */
var maxNumberOfAlloys = function(n, k, budget, composition, stock, cost) {
    const ok = (machines) => {
        for (const comp of composition) {
            let spend = 0n;
            for (let i = 0; i < n; i++) {
                const need = BigInt(machines) * BigInt(comp[i]) - BigInt(stock[i]);
                if (need > 0n) spend += need * BigInt(cost[i]);
            }
            if (spend <= BigInt(budget)) return true;
        }
        return false;
    };
    let lo = 0n, hi = 1000000000n, ans = 0n;
    while (lo <= hi) {
        const mid = (lo + hi) / 2n;
        if (ok(mid)) { ans = mid; lo = mid + 1n; }
        else hi = mid - 1n;
    }
    return Number(ans);
};
