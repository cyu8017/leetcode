<?php
// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $rollMax
     * @return Integer
     */
    function dieSimulator($n, $rollMax) {
        $mod = 1000000007;
        $dp = [];
        for ($j = 0; $j < 6; $j++) {
            $dp[$j] = array_fill(0, $rollMax[$j] + 1, 0);
            $dp[$j][1] = 1;
        }
        for ($t = 1; $t < $n; $t++) {
            $totals = [];
            for ($j = 0; $j < 6; $j++) $totals[$j] = array_sum($dp[$j]) % $mod;
            $nxt = [];
            $sumAll = array_sum($totals) % $mod;
            for ($j = 0; $j < 6; $j++) {
                $nxt[$j] = array_fill(0, count($dp[$j]), 0);
                $nxt[$j][1] = ($sumAll - $totals[$j] + $mod) % $mod;
                for ($run = 2; $run < count($dp[$j]); $run++) {
                    $nxt[$j][$run] = $dp[$j][$run - 1];
                }
            }
            $dp = $nxt;
        }
        $ans = 0;
        foreach ($dp as $row) $ans = ($ans + array_sum($row)) % $mod;
        return $ans;
    }
}
