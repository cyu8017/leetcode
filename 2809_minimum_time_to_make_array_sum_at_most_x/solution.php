<?php
// LeetCode 2809 - Minimum Time to Make Array Sum At Most x
// https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

class Solution {
    function minimumTime($nums1, $nums2, $x) {
        $n = count($nums1);
        $arr = [];
        $sum1 = 0;
        $sum2 = 0;
        for ($i = 0; $i < $n; $i++) {
            $arr[] = [$nums1[$i], $nums2[$i]];
            $sum1 += $nums1[$i];
            $sum2 += $nums2[$i];
        }
        usort($arr, function($a, $b) { return $a[1] <=> $b[1]; });
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j >= 1; $j--) {
                $dp[$j] = max($dp[$j], $dp[$j - 1] + $arr[$i][0] + $j * $arr[$i][1]);
            }
        }
        for ($t = 0; $t <= $n; $t++) {
            if ($sum1 + $sum2 * $t - $dp[$t] <= $x) return $t;
        }
        return -1;
    }
}
