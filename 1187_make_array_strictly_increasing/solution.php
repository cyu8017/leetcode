<?php
// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function makeArrayIncreasing($arr1, $arr2) {
        $arr2 = array_values(array_unique($arr2));
        sort($arr2);
        $dp = [-1 => 0];
        foreach ($arr1 as $num) {
            $newDp = [];
            foreach ($dp as $prev => $ops) {
                if ($num > $prev) {
                    $newDp[$num] = min($newDp[$num] ?? PHP_INT_MAX, $ops);
                }
                $lo = 0; $hi = count($arr2);
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if ($arr2[$mid] <= $prev) $lo = $mid + 1;
                    else $hi = $mid;
                }
                if ($lo < count($arr2)) {
                    $chosen = $arr2[$lo];
                    $newDp[$chosen] = min($newDp[$chosen] ?? PHP_INT_MAX, $ops + 1);
                }
            }
            $dp = $newDp;
            if (empty($dp)) return -1;
        }
        return min($dp);
    }
}
