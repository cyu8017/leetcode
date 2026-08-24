<?php
// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

class Solution {
    function scoreBalance($s) {
        $l = 0;
        $r = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $r += (ord($s[$i]) - 97) + 1;
        for ($i = 0; $i + 1 < $n; $i++) {
            $x = (ord($s[$i]) - 97) + 1;
            $l += $x;
            $r -= $x;
            if ($l === $r) return true;
        }
        return false;
    }
}
