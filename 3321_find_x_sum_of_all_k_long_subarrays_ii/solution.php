<?php
// LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

class Solution {
    function findXSum($nums, $k, $x) {
        $n = count($nums);
        $ans = [];
        for ($i = 0; $i <= $n - $k; $i++) {
            $freq = [];
            for ($j = $i; $j < $i + $k; $j++) $freq[$nums[$j]] = ($freq[$nums[$j]] ?? 0) + 1;
            $arr = [];
            foreach ($freq as $key => $val) $arr[] = [$key, $val];
            usort($arr, function($A, $B) {
                if ($B[1] !== $A[1]) return $B[1] <=> $A[1];
                return $B[0] <=> $A[0];
            });
            $lim = min($x, count($arr));
            $keep = [];
            for ($t = 0; $t < $lim; $t++) $keep[$arr[$t][0]] = true;
            $sum = 0;
            for ($j = $i; $j < $i + $k; $j++) if (isset($keep[$nums[$j]])) $sum += $nums[$j];
            $ans[$i] = $sum;
        }
        return $ans;
    }
}
