<?php
// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function primePalindrome($n) {
        if ($n <= 2) return 2;
        if ($n <= 3) return 3;
        if ($n <= 5) return 5;
        if ($n <= 7) return 7;
        if ($n <= 11) return 11;
        $isPrime = function($x) {
            if ($x < 2) return false;
            if ($x % 2 === 0) return $x === 2;
            for ($d = 3; $d * $d <= $x; $d += 2) if ($x % $d === 0) return false;
            return true;
        };
        for ($length = 1; $length <= 5; $length++) {
            $start = (int)pow(10, $length - 1);
            $end = (int)pow(10, $length);
            for ($root = $start; $root < $end; $root++) {
                $s = (string)$root;
                $pal = $s;
                for ($i = strlen($s) - 2; $i >= 0; $i--) $pal .= $s[$i];
                $val = intval($pal);
                if ($val >= $n && $isPrime($val)) return $val;
            }
        }
        return 0;
    }
}
