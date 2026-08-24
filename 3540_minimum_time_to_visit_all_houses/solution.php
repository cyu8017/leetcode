<?php
// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

class Solution {
    function minTotalTime($forward, $backward, $queries) {
        $n = count($forward);
        $sumB = 0;
        foreach ($backward as $v) $sumB += $v;
        $pf = array_fill(0, $n + 1, 0);
        $pb = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pf[$i + 1] = $pf[$i] + $forward[$i];
            $pb[$i + 1] = $pb[$i] + $backward[$i];
        }
        $ans = 0;
        $pos = 0;
        foreach ($queries as $q) {
            $r = 0;
            if ($q < $pos) $r = $pf[$n];
            $r += $pf[$q] - $pf[$pos];
            $l = 0;
            if ($q > $pos) $l = $sumB;
            $l += $pb[$pos] - $pb[$q];
            $ans += min($l, $r);
            $pos = $q;
        }
        return $ans;
    }
}
