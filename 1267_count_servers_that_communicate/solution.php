<?php
// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

class Solution {
    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countServers($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $rows = array_fill(0, $m, 0);
        $cols = array_fill(0, $n, 0);
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c]) { $rows[$r]++; $cols[$c]++; }
            }
        }
        $ans = 0;
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                if ($grid[$r][$c] && ($rows[$r] > 1 || $cols[$c] > 1)) $ans++;
            }
        }
        return $ans;
    }
}
