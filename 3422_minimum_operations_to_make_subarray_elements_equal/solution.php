<?php
// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

class Solution {
    function minOperations($nums, $k) {
        $n = count($nums);
        $ans = PHP_INT_MAX;
        for ($i = 0; $i + $k <= $n; $i++) {
            $sub = array_slice($nums, $i, $k);
            sort($sub);
            $med = $sub[intdiv($k, 2)];
            $cost = 0;
            foreach ($sub as $x) $cost += abs($x - $med);
            if ($cost < $ans) $ans = $cost;
        }
        return $ans;
    }
}
