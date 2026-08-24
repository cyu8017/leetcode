<?php
// LeetCode 2256 - Minimum Average Difference
// https://leetcode.com/problems/minimum-average-difference/

class Solution {
    function minimumAverageDifference($nums) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $v) $total += $v;
        $left = 0;
        $bestDiff = PHP_INT_MAX;
        $bestIdx = 0;
        for ($i = 0; $i < $n; $i++) {
            $left += $nums[$i];
            $leftAvg = intdiv($left, $i + 1);
            $rightAvg = 0;
            if ($i !== $n - 1) $rightAvg = intdiv($total - $left, $n - $i - 1);
            $diff = abs($leftAvg - $rightAvg);
            if ($diff < $bestDiff) { $bestDiff = $diff; $bestIdx = $i; }
        }
        return $bestIdx;
    }
}
