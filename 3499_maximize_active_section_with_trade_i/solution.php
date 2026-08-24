<?php
// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

class Solution {
    function maxActiveSectionsAfterTrade($s) {
        $ones = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === "1") $ones++;
        $zeros = [];
        for ($i = 0; $i < $n; ) {
            if ($s[$i] !== "0") { $i++; continue; }
            $j = $i;
            while ($j < $n && $s[$j] === "0") $j++;
            $zeros[] = [$i, $j - 1];
            $i = $j;
        }
        $best = 0;
        for ($i = 0; $i + 1 < count($zeros); $i++) {
            $gain = ($zeros[$i][1] - $zeros[$i][0] + 1) + ($zeros[$i + 1][1] - $zeros[$i + 1][0] + 1);
            if ($gain > $best) $best = $gain;
        }
        return $ones + $best;
    }
}
