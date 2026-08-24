<?php
// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution {
    function subarraysDivByK($nums, $k) {
        $count = [0 => 1];
        $prefix = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $prefix = (($prefix + $x) % $k + $k) % $k;
            $ans += $count[$prefix] ?? 0;
            $count[$prefix] = ($count[$prefix] ?? 0) + 1;
        }
        return $ans;
    }
}
