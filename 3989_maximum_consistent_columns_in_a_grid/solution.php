<?php
// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

class Solution {
    function maxConsistentColumns($grid, $limit) {
        $m = count($grid);
        $n = count($grid[0]);
        $dp = array_fill(0, $n, 0);
        $ans = 1;
        for ($j = 0; $j < $n; $j++) {
            $dp[$j] = 1;
            for ($i = 0; $i < $j; $i++) {
                if ($dp[$i] + 1 <= $dp[$j]) continue;
                $ok = true;
                for ($r = 0; $r < $m; $r++) {
                    $d = abs($grid[$r][$j] - $grid[$r][$i]);
                    if ($d > $limit) { $ok = false; break; }
                }
                if ($ok) $dp[$j] = $dp[$i] + 1;
            }
            if ($dp[$j] > $ans) $ans = $dp[$j];
        }
        return $ans;
    }
}
