<?php
// LeetCode 0465 - Optimal Account Balancing
// https://leetcode.com/problems/optimal-account-balancing/

class Solution {
    /**
     * @param int[][] $transactions
     * @return int
     */
    function minTransfers($transactions) {
        return $this->min_transfers($transactions);
    }

    /**
     * @param int[][] $transactions
     * @return int
     */
    function min_transfers($transactions) {
        $balances = [];
        foreach ($transactions as [$source, $target, $amount]) {
            $balances[$source] = ($balances[$source] ?? 0) - $amount;
            $balances[$target] = ($balances[$target] ?? 0) + $amount;
        }

        $debts = array_values(array_filter($balances, fn($balance) => $balance !== 0));
        return $this->dfs($debts, 0);
    }

    /**
     * @param int[] $debts
     */
    private function dfs(array &$debts, int $index): int {
        while ($index < count($debts) && $debts[$index] === 0) {
            $index++;
        }
        if ($index === count($debts)) {
            return 0;
        }

        $best = count($debts);
        for ($nextIndex = $index + 1; $nextIndex < count($debts); $nextIndex++) {
            if ($debts[$index] * $debts[$nextIndex] < 0) {
                $debts[$nextIndex] += $debts[$index];
                $best = min($best, 1 + $this->dfs($debts, $index + 1));
                $debts[$nextIndex] -= $debts[$index];
            }
        }

        return $best;
    }
}
