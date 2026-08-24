<?php
// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

class Solution {
    function maxSum($nums, $m, $k) {
        $freq = [];
        $sum = 0;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (!isset($freq[$nums[$i]])) $freq[$nums[$i]] = 0;
            $freq[$nums[$i]]++;
            $sum += $nums[$i];
            if ($i >= $k) {
                $out = $nums[$i - $k];
                $sum -= $out;
                $freq[$out]--;
                if ($freq[$out] === 0) unset($freq[$out]);
            }
            if ($i >= $k - 1 && count($freq) >= $m && $sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
