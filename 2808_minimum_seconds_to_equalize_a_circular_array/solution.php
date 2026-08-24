<?php
// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

class Solution {
    function minimumSeconds($nums) {
        $n = count($nums);
        $pos = [];
        for ($i = 0; $i < $n; $i++) $pos[$nums[$i]][] = $i;
        $ans = $n;
        foreach ($pos as $p) {
            $maxGap = 0;
            $m = count($p);
            for ($i = 0; $i < $m; $i++) {
                $gap = ($i + 1 < $m) ? $p[$i + 1] - $p[$i] : $p[0] + $n - $p[$i];
                $maxGap = max($maxGap, intdiv($gap, 2));
            }
            $ans = min($ans, $maxGap);
        }
        return $ans;
    }
}
