<?php
// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

class Solution {
    private function fRel($a, $b) {
        if ($a === $b) return 0;
        return $a < $b ? 1 : -1;
    }

    function countMatchingSubarrays($nums, $pattern) {
        $n = count($nums);
        $m = count($pattern);
        $ans = 0;
        for ($i = 0; $i < $n - $m; $i++) {
            $ok = 1;
            for ($k = 0; $k < $m && $ok !== 0; $k++) {
                if ($this->fRel($nums[$i + $k], $nums[$i + $k + 1]) !== $pattern[$k]) $ok = 0;
            }
            $ans += $ok;
        }
        return $ans;
    }
}
