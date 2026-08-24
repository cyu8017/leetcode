<?php
// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

class Solution {
    function countBinarySubstrings($s) {
        $prev = 0;
        $cur = 1;
        $ans = 0;
        $n = strlen($s);
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] === $s[$i - 1]) $cur++;
            else {
                $ans += min($prev, $cur);
                $prev = $cur;
                $cur = 1;
            }
        }
        return $ans + min($prev, $cur);
    }
}
