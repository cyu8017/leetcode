<?php
// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution {
    function numberOfSpecialChars($word) {
        $s = array_fill(0, 128, false);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) $s[ord($word[$i])] = true;
        $ans = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($s[97 + $i] && $s[65 + $i]) $ans++;
        }
        return $ans;
    }
}
