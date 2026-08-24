<?php
// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

class Solution {
    function solveQueries($nums, $queries) {
        $n = count($nums);
        $pos = [];
        for ($i = 0; $i < $n; $i++) {
            if (!isset($pos[$nums[$i]])) $pos[$nums[$i]] = [];
            $pos[$nums[$i]][] = $i;
        }
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $idx = $queries[$qi];
            $x = $nums[$idx];
            $arr = $pos[$x];
            if (count($arr) === 1) { $ans[$qi] = -1; continue; }
            $best = $n;
            foreach ($arr as $p) {
                if ($p === $idx) continue;
                $d = abs($p - $idx);
                $d = min($d, $n - $d);
                if ($d < $best) $best = $d;
            }
            $ans[$qi] = $best;
        }
        return $ans;
    }
}
