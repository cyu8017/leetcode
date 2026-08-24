<?php
// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/

class Solution {
    function completePrime($num) {
        $isPrime = function($x) {
            if ($x < 2) return false;
            for ($i = 2; $i * $i <= $x; $i++) if ($x % $i === 0) return false;
            return true;
        };
        $s = strval($num);
        $x = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $x = $x * 10 + (ord($s[$i]) - 48);
            if (!$isPrime($x)) return false;
        }
        $x = 0;
        $p = 1;
        for ($i = $len - 1; $i >= 0; $i--) {
            $x = $p * (ord($s[$i]) - 48) + $x;
            $p *= 10;
            if (!$isPrime($x)) return false;
        }
        return true;
    }
}
