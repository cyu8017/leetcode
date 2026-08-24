<?php
// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution {
    function longestContinuousSubstring($s) {
        $ans = 1;
        $cur = 1;
        $n = strlen($s);
        for ($i = 1; $i < $n; $i++) {
            if (ord($s[$i]) === ord($s[$i - 1]) + 1) {
                $cur++;
                $ans = max($ans, $cur);
            } else {
                $cur = 1;
            }
        }
        return $ans;
    }
}
