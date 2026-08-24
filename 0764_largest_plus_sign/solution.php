<?php
// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

class Solution {
    function orderOfLargestPlusSign($n, $mines) {
        $banned = [];
        foreach ($mines as $mine) $banned[$mine[0] * $n + $mine[1]] = true;
        $arms = array_fill(0, $n, array_fill(0, $n, 0));
        $best = 0;
        for ($r = 0; $r < $n; $r++) {
            $count = 0;
            for ($c = 0; $c < $n; $c++) {
                $count = isset($banned[$r * $n + $c]) ? 0 : $count + 1;
                $arms[$r][$c] = $count;
            }
            $count = 0;
            for ($c = $n - 1; $c >= 0; $c--) {
                $count = isset($banned[$r * $n + $c]) ? 0 : $count + 1;
                $arms[$r][$c] = min($arms[$r][$c], $count);
            }
        }
        for ($c = 0; $c < $n; $c++) {
            $count = 0;
            for ($r = 0; $r < $n; $r++) {
                $count = isset($banned[$r * $n + $c]) ? 0 : $count + 1;
                $arms[$r][$c] = min($arms[$r][$c], $count);
            }
            $count = 0;
            for ($r = $n - 1; $r >= 0; $r--) {
                $count = isset($banned[$r * $n + $c]) ? 0 : $count + 1;
                $arms[$r][$c] = min($arms[$r][$c], $count);
                $best = max($best, $arms[$r][$c]);
            }
        }
        return $best;
    }
}
