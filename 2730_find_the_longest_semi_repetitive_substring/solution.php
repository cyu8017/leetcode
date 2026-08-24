<?php
// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution {
    function longestSemiRepetitiveSubstring($s) {
        $ans = 0;
        $left = 0;
        $lastPair = -1;
        $n = strlen($s);
        for ($right = 0; $right < $n; $right++) {
            if ($right > 0 && $s[$right] === $s[$right - 1]) {
                if ($lastPair >= $left) $left = $lastPair + 1;
                $lastPair = $right - 1;
            }
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
