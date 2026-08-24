<?php
// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

class Solution {
    function simulationResult($windows, $queries) {
        $n = count($windows);
        $s = array_fill(0, $n + 1, false);
        $ans = [];
        for ($i = count($queries) - 1; $i >= 0; $i--) {
            $q = $queries[$i];
            if (!$s[$q]) { $s[$q] = true; $ans[] = $q; }
        }
        foreach ($windows as $w) if (!$s[$w]) $ans[] = $w;
        return $ans;
    }
}
