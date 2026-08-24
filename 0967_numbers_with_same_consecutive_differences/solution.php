<?php
// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution {
    function numsSameConsecDiff($n, $k) {
        $ans = [];
        $dfs = function ($num, $length) use (&$dfs, &$ans, $n, $k) {
            if ($length === $n) {
                $ans[] = $num;
                return;
            }
            $last = $num % 10;
            $nexts = [$last - $k];
            if ($k !== 0) $nexts[] = $last + $k;
            foreach ($nexts as $nxt) {
                if ($nxt >= 0 && $nxt <= 9) $dfs($num * 10 + $nxt, $length + 1);
            }
        };
        for ($start = 1; $start <= 9; $start++) $dfs($start, 1);
        return $ans;
    }
}
