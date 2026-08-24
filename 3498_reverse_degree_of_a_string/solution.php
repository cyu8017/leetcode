<?php
// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution {
    function reverseDegree($s) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++)
            $ans += (26 - (ord($s[$i]) - 97)) * ($i + 1);
        return $ans;
    }
}
