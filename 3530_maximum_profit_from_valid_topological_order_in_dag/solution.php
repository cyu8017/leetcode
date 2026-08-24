<?php
// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

class Solution {
    private function popcount($x) {
        $c = 0;
        while ($x !== 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function maxProfit($n, $edges, $score) {
        $need = array_fill(0, $n, 0);
        $dp = array_fill(0, 1 << $n, -1);
        $dp[0] = 0;
        foreach ($edges as $e) $need[$e[1]] |= 1 << $e[0];
        for ($mask = 0; $mask < (1 << $n); $mask++) {
            if ($dp[$mask] < 0) continue;
            $pos = $this->popcount($mask) + 1;
            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) !== 0) continue;
                if (($mask & $need[$i]) === $need[$i]) {
                    $nm = $mask | (1 << $i);
                    $v = $dp[$mask] + $score[$i] * $pos;
                    if ($v > $dp[$nm]) $dp[$nm] = $v;
                }
            }
        }
        return $dp[(1 << $n) - 1];
    }
}
