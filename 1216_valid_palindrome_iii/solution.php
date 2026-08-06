<?php
// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Boolean
     */
    function isValidPalindrome($s, $k) {
        $n = strlen($s);
        if ($n === 0) return true;
        $dp = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $previous = 0;
            for ($j = $i + 1; $j < $n; $j++) {
                $old = $dp[$j];
                if ($s[$i] === $s[$j]) $dp[$j] = $previous;
                else $dp[$j] = 1 + min($dp[$j], $dp[$j - 1]);
                $previous = $old;
            }
        }
        return $dp[$n - 1] <= $k;
    }
}
