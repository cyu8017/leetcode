<?php
// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

class Solution {
    function longestValidSubstring($word, $forbidden) {
        $forbid = array_fill_keys($forbidden, true);
        $maxLen = 0;
        foreach ($forbidden as $f) $maxLen = max($maxLen, strlen($f));
        $ans = 0;
        $n = strlen($word);
        $right = $n - 1;
        for ($left = $n - 1; $left >= 0; $left--) {
            for ($k = $left; $k <= $right && $k - $left + 1 <= $maxLen; $k++) {
                if (isset($forbid[substr($word, $left, $k - $left + 1)])) {
                    $right = $k - 1;
                    break;
                }
            }
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
