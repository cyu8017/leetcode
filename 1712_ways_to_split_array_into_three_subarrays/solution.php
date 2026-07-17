<?php
// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function waysToSplit($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $prefix = [];
        $total = 0;
        foreach ($nums as $value) {
            $total += $value;
            $prefix[] = $total;
        }

        $lowerBound = function ($target, $lo, $hi) use ($prefix) {
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($prefix[$mid] < $target) {
                    $lo = $mid + 1;
                } else {
                    $hi = $mid;
                }
            }
            return $lo;
        };

        $upperBound = function ($target, $lo, $hi) use ($prefix) {
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($prefix[$mid] <= $target) {
                    $lo = $mid + 1;
                } else {
                    $hi = $mid;
                }
            }
            return $lo;
        };

        $ans = 0;
        for ($i = 0; $i < $n - 2; $i++) {
            $left = $prefix[$i];
            $lo = $lowerBound(2 * $left, $i + 1, $n - 1);
            $hi = $upperBound(intdiv($total + $left, 2), $lo, $n - 1);
            $ans = ($ans + $hi - $lo) % $mod;
        }
        return $ans;
    }
}
