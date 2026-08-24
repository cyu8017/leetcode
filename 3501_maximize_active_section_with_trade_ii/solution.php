<?php
// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

class Solution {
    function maxActiveSectionsAfterTrade($s, $queries) {
        $ones = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === "1") $ones++;
        $ans = array_fill(0, count($queries), $ones);
        return $ans;
    }
}
