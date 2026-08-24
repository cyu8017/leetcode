<?php
// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

class Solution {
    function makePalindrome($s) {
        $diff = 0;
        $n = strlen($s);
        for ($i = 0, $j = $n - 1; $i < $j; ++$i, --$j) {
            if ($s[$i] !== $s[$j]) {
                $diff++;
                if ($diff > 2) return false;
            }
        }
        return true;
    }
}
