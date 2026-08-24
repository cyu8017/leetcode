<?php
// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

class Solution {
    function subarrayMajority($nums, $queries) {
        $ans = array_fill(0, count($queries), 0);
        $qn = count($queries);
        for ($qi = 0; $qi < $qn; $qi++) {
            $l = $queries[$qi][0];
            $r = $queries[$qi][1];
            $t = $queries[$qi][2];
            $cnt = [];
            for ($i = $l; $i <= $r; $i++) {
                if (!isset($cnt[$nums[$i]])) $cnt[$nums[$i]] = 0;
                $cnt[$nums[$i]]++;
            }
            $best = -1;
            $bestC = 0;
            foreach ($cnt as $v => $c) {
                if ($c >= $t && ($c > $bestC || ($c === $bestC && ($best === -1 || $v < $best)))) {
                    $bestC = $c;
                    $best = $v;
                }
            }
            $ans[$qi] = $best;
        }
        return $ans;
    }
}
