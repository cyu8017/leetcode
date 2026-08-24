<?php
// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution {
    function numberOfSpecialChars($word) {
        $first = array_fill(0, 128, 0);
        $last = array_fill(0, 128, 0);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $c = ord($word[$i]);
            if ($first[$c] === 0) $first[$c] = $i + 1;
            $last[$c] = $i + 1;
        }
        $ans = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($last[97 + $i] > 0 && $last[97 + $i] < $first[65 + $i]) $ans++;
        }
        return $ans;
    }
}
