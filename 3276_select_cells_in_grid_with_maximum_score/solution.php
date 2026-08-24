<?php
// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

class Solution {
    function maxScore($grid) {
        $m = count($grid);
        $vals = [];
        for ($i = 0; $i < $m; $i++) {
            $seen = [];
            foreach ($grid[$i] as $v) {
                if (!isset($seen[$v])) {
                    $seen[$v] = true;
                    if (!isset($vals[$v])) $vals[$v] = [];
                    $vals[$v][] = $i;
                }
            }
        }
        $arr = array_keys($vals);
        rsort($arr);
        $N = 1 << $m;
        $dp = array_fill(0, $N, 0);
        foreach ($arr as $v) {
            $ndp = $dp;
            foreach ($vals[$v] as $r) {
                $bit = 1 << $r;
                for ($mask = 0; $mask < $N; $mask++) {
                    if (($mask & $bit) !== 0) continue;
                    $cand = $dp[$mask] + $v;
                    $nmask = $mask | $bit;
                    if ($cand > $ndp[$nmask]) $ndp[$nmask] = $cand;
                }
            }
            $dp = $ndp;
        }
        $ans = 0;
        foreach ($dp as $x) $ans = max($ans, $x);
        return $ans;
    }
}
