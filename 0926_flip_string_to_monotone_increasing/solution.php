<?php
// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution {
    function minFlipsMonoIncr($s) {
        $ones = 0;
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === "1") $ones++;
            else $ans = min($ans + 1, $ones);
        }
        return $ans;
    }
}
