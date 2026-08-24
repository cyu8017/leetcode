<?php
// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function kIncreasing($arr, $k) {
        $ans = 0;
        $n = count($arr);
        for ($start = 0; $start < $k; $start++) {
            $seq = [];
            for ($i = $start; $i < $n; $i += $k) $seq[] = $arr[$i];
            $tails = [];
            foreach ($seq as $x) {
                $lo = 0;
                $hi = count($tails);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($tails[$mid] <= $x) $lo = $mid + 1;
                    else $hi = $mid;
                }
                if ($lo === count($tails)) $tails[] = $x;
                else $tails[$lo] = $x;
            }
            $ans += count($seq) - count($tails);
        }
        return $ans;
    }
}
