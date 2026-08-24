<?php
// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumDeletions($nums) {
        $n = count($nums);
        $mi = 0;
        $ma = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] < $nums[$mi]) $mi = $i;
            if ($nums[$i] > $nums[$ma]) $ma = $i;
        }
        if ($mi > $ma) {
            $t = $mi;
            $mi = $ma;
            $ma = $t;
        }
        return min($ma + 1, $n - $mi, $mi + 1 + $n - $ma);
    }
}
