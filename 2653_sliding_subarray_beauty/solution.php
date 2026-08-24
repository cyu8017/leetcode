<?php
// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

class Solution {
    function getSubarrayBeauty($nums, $k, $x) {
        $freq = array_fill(0, 101, 0);
        $ans = array_fill(0, count($nums) - $k + 1, 0);
        for ($i = 0; $i < count($nums); $i++) {
            $freq[$nums[$i] + 50]++;
            if ($i >= $k) $freq[$nums[$i - $k] + 50]--;
            if ($i >= $k - 1) {
                $need = $x;
                $val = 0;
                for ($j = 0; $j < 50; $j++) {
                    $need -= $freq[$j];
                    if ($need <= 0) { $val = $j - 50; break; }
                }
                $ans[$i - $k + 1] = $val;
            }
        }
        return $ans;
    }
}
