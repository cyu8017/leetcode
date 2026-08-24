<?php
// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

class Solution {
    function reverseSubarrays($nums, $k) {
        $n = count($nums);
        $m = intdiv($n, $k);
        for ($i = 0; $i < $n; $i += $m) {
            $lo = $i;
            $hi = $i + $m - 1;
            while ($lo < $hi) {
                $t = $nums[$lo];
                $nums[$lo] = $nums[$hi];
                $nums[$hi] = $t;
                $lo++;
                $hi--;
            }
        }
        return $nums;
    }
}
