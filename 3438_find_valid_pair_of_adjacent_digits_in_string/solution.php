<?php
// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

class Solution {
    function findValidPair($s) {
        $freq = array_fill(0, 10, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 48]++;
        for ($i = 0; $i + 1 < $n; $i++) {
            $a = ord($s[$i]) - 48;
            $b = ord($s[$i + 1]) - 48;
            if ($a !== $b && $freq[$a] === $a && $freq[$b] === $b) return substr($s, $i, 2);
        }
        return "";
    }
}
