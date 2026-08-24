<?php
// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

class Solution {
    function subarraySum($nums, $k) {
        $counts = [0 => 1];
        $prefix = 0;
        $answer = 0;
        foreach ($nums as $num) {
            $prefix += $num;
            $answer += $counts[$prefix - $k] ?? 0;
            $counts[$prefix] = ($counts[$prefix] ?? 0) + 1;
        }
        return $answer;
    }
}
