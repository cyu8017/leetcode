<?php
// LeetCode 3918 - Sum of Primes Between Number and Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

class Solution {
    static $isPrime = null;
    function Init() {
        if (self::$isPrime !== null) return;
        self::$isPrime = array_fill(0, 1001, true);
        self::$isPrime[0] = self::$isPrime[1] = false;
        for ($i = 2; $i * $i <= 1000; $i++) {
            if (self::$isPrime[$i]) {
                for ($j = $i * $i; $j <= 1000; $j += $i) self::$isPrime[$j] = false;
            }
        }
    }
    function sumOfPrimesInRange($n) {
        $this->Init();
        $r = 0;
        for ($x = $n; $x > 0; $x = intdiv($x, 10)) $r = $r * 10 + $x % 10;
        $low = min($n, $r);
        $high = max($n, $r);
        $ans = 0;
        for ($x = $low; $x <= $high; $x++) {
            if (self::$isPrime[$x]) $ans += $x;
        }
        return $ans;
    }
}
