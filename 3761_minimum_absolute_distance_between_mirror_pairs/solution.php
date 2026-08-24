<?php
// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

class Solution {
    function minMirrorPairDistance($nums) {
        $reverse = function($x) {
            $y = 0;
            for (; $x > 0; $x = intdiv($x, 10)) $y = $y * 10 + $x % 10;
            return $y;
        };
        $n = count($nums);
        $pos = [];
        $ans = $n + 1;
        for ($i = 0; $i < $n; $i++) {
            if (isset($pos[$nums[$i]])) $ans = min($ans, $i - $pos[$nums[$i]]);
            $pos[$reverse($nums[$i])] = $i;
        }
        return $ans > $n ? -1 : $ans;
    }
}
