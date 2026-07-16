// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

class Solution {
    minTransfers(transactions) {
        const balances = new Map();
        for (const [source, target, amount] of transactions) {
            balances.set(source, (balances.get(source) || 0) - amount);
            balances.set(target, (balances.get(target) || 0) + amount);
        }
        const debts = [...balances.values()].filter((balance) => balance !== 0);

        const dfs = (index) => {
            while (index < debts.length && debts[index] === 0) index += 1;
            if (index === debts.length) return 0;
            let best = debts.length;
            for (let nextIndex = index + 1; nextIndex < debts.length; nextIndex += 1) {
                if (debts[index] * debts[nextIndex] < 0) {
                    debts[nextIndex] += debts[index];
                    best = Math.min(best, 1 + dfs(index + 1));
                    debts[nextIndex] -= debts[index];
                }
            }
            return best;
        };

        return dfs(0);
    }
}

module.exports = { Solution };
