<?php
// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

class Solution {
    function longestLine($mat) {
        if (count($mat) === 0 || count($mat[0]) === 0) return 0;
        $rows = count($mat);
        $cols = count($mat[0]);
        $dp = [];
        for ($r = 0; $r < $rows; ++$r) {
            $dp[$r] = [];
            for ($c = 0; $c < $cols; ++$c) $dp[$r][$c] = [0, 0, 0, 0];
        }
        $best = 0;
        for ($r = 0; $r < $rows; ++$r) {
            for ($c = 0; $c < $cols; ++$c) {
                if ($mat[$r][$c] === 0) continue;
                $dp[$r][$c][0] = ($c > 0 ? $dp[$r][$c - 1][0] : 0) + 1;
                $dp[$r][$c][1] = ($r > 0 ? $dp[$r - 1][$c][1] : 0) + 1;
                $dp[$r][$c][2] = ($r > 0 && $c > 0 ? $dp[$r - 1][$c - 1][2] : 0) + 1;
                $dp[$r][$c][3] = ($r > 0 && $c + 1 < $cols ? $dp[$r - 1][$c + 1][3] : 0) + 1;
                for ($d = 0; $d < 4; ++$d) $best = max($best, $dp[$r][$c][$d]);
            }
        }
        return $best;
    }
}
