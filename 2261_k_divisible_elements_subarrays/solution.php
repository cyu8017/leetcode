<?php
// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

class Solution {
    function countDistinct($nums, $k, $p) {
        $n = count($nums);
        $seen = [];
        for ($i = 0; $i < $n; $i++) {
            $div = 0;
            $key = '';
            for ($j = $i; $j < $n; $j++) {
                if ($nums[$j] % $p === 0) $div++;
                if ($div > $k) break;
                $key .= ($nums[$j] + 1) . ',';
                $seen[$key] = true;
            }
        }
        return count($seen);
    }
}
