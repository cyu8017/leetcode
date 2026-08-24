<?php
// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution {
    function findNumberOfLIS($nums) {
        $n = count($nums);
        $lengths = array_fill(0, $n, 1);
        $counts = array_fill(0, $n, 1);
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $i; ++$j) {
                if ($nums[$j] >= $nums[$i]) continue;
                if ($lengths[$j] + 1 > $lengths[$i]) {
                    $lengths[$i] = $lengths[$j] + 1;
                    $counts[$i] = $counts[$j];
                } elseif ($lengths[$j] + 1 === $lengths[$i]) {
                    $counts[$i] += $counts[$j];
                }
            }
        }
        $longest = 0;
        foreach ($lengths as $length) $longest = max($longest, $length);
        $answer = 0;
        for ($i = 0; $i < $n; ++$i) if ($lengths[$i] === $longest) $answer += $counts[$i];
        return $answer;
    }
}
