<?php
// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

class Solution {
    function scoreOfString($s) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 1; $i < $n; $i++)
            $ans += abs(ord($s[$i - 1]) - ord($s[$i]));
        return $ans;
    }
}
