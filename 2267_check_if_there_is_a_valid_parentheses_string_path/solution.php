<?php
// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

class Solution {
    function hasValidPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        if (($m + $n - 1) % 2 === 1 || $grid[0][0] === ')' || $grid[$m - 1][$n - 1] === '(') return false;
        $vis = [];
        $dfs = function($r, $c, $bal) use (&$dfs, &$vis, $m, $n, $grid) {
            if ($r >= $m || $c >= $n) return false;
            $bal += ($grid[$r][$c] === '(') ? 1 : -1;
            if ($bal < 0) return false;
            if ($r === $m - 1 && $c === $n - 1) return $bal === 0;
            $k = (($r * $n + $c) << 10) | $bal;
            if (isset($vis[$k])) return false;
            $vis[$k] = true;
            return $dfs($r + 1, $c, $bal) || $dfs($r, $c + 1, $bal);
        };
        return $dfs(0, 0, 0);
    }
}
