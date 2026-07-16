// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

using System.Linq;

public class Solution {
    public int MinTransfers(int[][] transactions) {
        Dictionary<int, int> balances = new();
        foreach (int[] transaction in transactions) {
            int source = transaction[0];
            int target = transaction[1];
            int amount = transaction[2];
            balances[source] = balances.GetValueOrDefault(source) - amount;
            balances[target] = balances.GetValueOrDefault(target) + amount;
        }

        int[] debts = balances.Values.Where(value => value != 0).ToArray();
        return Dfs(debts, 0);
    }

    private int Dfs(int[] debts, int index) {
        while (index < debts.Length && debts[index] == 0) {
            index++;
        }
        if (index == debts.Length) {
            return 0;
        }
        int best = debts.Length;
        for (int nextIndex = index + 1; nextIndex < debts.Length; nextIndex++) {
            if ((long)debts[index] * debts[nextIndex] < 0) {
                debts[nextIndex] += debts[index];
                best = Math.Min(best, 1 + Dfs(debts, index + 1));
                debts[nextIndex] -= debts[index];
            }
        }
        return best;
    }
}
