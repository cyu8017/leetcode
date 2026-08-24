<?php
// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

class Solution {
    function maximumCount($nums, $queries) {
        $mx = 0;
        foreach ($nums as $v) $mx = max($mx, $v);
        foreach ($queries as $q) $mx = max($mx, $q[1]);
        $isP = array_fill(0, $mx + 1, false);
        for ($i = 2; $i <= $mx; $i++) $isP[$i] = true;
        for ($i = 2; $i * $i <= $mx; $i++) {
            if ($isP[$i]) for ($j = $i * $i; $j <= $mx; $j += $i) $isP[$j] = false;
        }
        $ans = array_fill(0, count($queries), 0);
        for ($qi = 0; $qi < count($queries); $qi++) {
            $nums[$queries[$qi][0]] = $queries[$qi][1];
            $best = 0;
            $left = [];
            $right = [];
            foreach ($nums as $v) if ($v <= $mx && $isP[$v]) $right[$v] = ($right[$v] ?? 0) + 1;
            for ($i = 0; $i < count($nums) - 1; $i++) {
                $v = $nums[$i];
                if ($v <= $mx && $isP[$v]) {
                    $left[$v] = ($left[$v] ?? 0) + 1;
                    $c = $right[$v] - 1;
                    if ($c === 0) unset($right[$v]);
                    else $right[$v] = $c;
                }
                $best = max($best, count($left) + count($right));
            }
            $ans[$qi] = $best;
        }
        return $ans;
    }
}
