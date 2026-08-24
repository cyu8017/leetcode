<?php
// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution {
    function percentageLetter($s, $letter) {
        $cnt = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($s[$i] === $letter) $cnt++;
        return intdiv($cnt * 100, $n);
    }
}
