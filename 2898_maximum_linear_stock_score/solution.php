<?php
// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

class Solution {
    function maxScore($prices) {
        $best = [];
        $ans = 0;
        $n = count($prices);
        for ($i = 0; $i < $n; $i++) {
            $key = $prices[$i] - ($i + 1);
            $cand = ($best[$key] ?? 0) + $prices[$i];
            if ($cand > ($best[$key] ?? 0)) $best[$key] = $cand;
            if ($best[$key] > $ans) $ans = $best[$key];
        }
        return $ans;
    }
}
