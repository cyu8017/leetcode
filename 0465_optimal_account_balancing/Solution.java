// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minTransfers(int[][] transactions) {
        Map<Integer, Integer> balances = new HashMap<>();
        for (int[] transaction : transactions) {
            int source = transaction[0];
            int target = transaction[1];
            int amount = transaction[2];
            balances.put(source, balances.getOrDefault(source, 0) - amount);
            balances.put(target, balances.getOrDefault(target, 0) + amount);
        }

        int[] debts = balances.values().stream().filter(value -> value != 0).mapToInt(Integer::intValue).toArray();
        return dfs(debts, 0);
    }

    private int dfs(int[] debts, int index) {
        while (index < debts.length && debts[index] == 0) {
            index++;
        }
        if (index == debts.length) {
            return 0;
        }
        int best = debts.length;
        for (int nextIndex = index + 1; nextIndex < debts.length; nextIndex++) {
            if ((long) debts[index] * debts[nextIndex] < 0) {
                debts[nextIndex] += debts[index];
                best = Math.min(best, 1 + dfs(debts, index + 1));
                debts[nextIndex] -= debts[index];
            }
        }
        return best;
    }
}
