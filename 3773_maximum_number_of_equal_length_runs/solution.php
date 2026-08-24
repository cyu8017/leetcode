<?php
// LeetCode 3773 - Maximum Number of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

class Solution {
    function maxSameLengthRuns($s) {
        $cnt = [];
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; ) {
            $j = $i + 1;
            while ($j < $n && $s[$j] === $s[$i]) $j++;
            $m = $j - $i;
            if (!isset($cnt[$m])) $cnt[$m] = 0;
            $cnt[$m]++;
            $ans = max($ans, $cnt[$m]);
            $i = $j;
        }
        return $ans;
    }
}
