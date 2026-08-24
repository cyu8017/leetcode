<?php
// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function maxSubsequence($nums, $k) {
        $n = count($nums);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$nums[$i], $i];
        usort($arr, function($a, $b) { return $b[0] - $a[0]; });
        $idx = array_slice($arr, 0, $k);
        usort($idx, function($a, $b) { return $a[1] - $b[1]; });
        $ans = [];
        foreach ($idx as $x) $ans[] = $nums[$x[1]];
        return $ans;
    }
}
