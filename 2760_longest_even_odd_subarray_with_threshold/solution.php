<?php
// LeetCode 2760 - Longest Even Odd Subarray With Threshold
// https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

class Solution {
    function longestAlternatingSubarray($nums, $threshold) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] % 2 !== 0 || $nums[$i] > $threshold) continue;
            $j = $i;
            while ($j + 1 < $n && $nums[$j + 1] <= $threshold && $nums[$j + 1] % 2 !== $nums[$j] % 2) $j++;
            $ans = max($ans, $j - $i + 1);
        }
        return $ans;
    }
}
