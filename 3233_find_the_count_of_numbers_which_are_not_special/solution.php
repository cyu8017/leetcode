<?php
// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

class Solution {
    private static $primes = null;

    function nonSpecialCount($l, $r) {
        $M = 31623;
        if (self::$primes === null) {
            $primes = array_fill(0, $M + 1, true);
            $primes[0] = false;
            $primes[1] = false;
            for ($i = 2; $i <= $M; $i++) {
                if ($primes[$i]) {
                    for ($j = $i * 2; $j <= $M; $j += $i) $primes[$j] = false;
                }
            }
            self::$primes = $primes;
        }
        $primes = self::$primes;
        $lo = (int)ceil(sqrt($l));
        $hi = (int)floor(sqrt($r));
        $cnt = 0;
        for ($i = $lo; $i <= $hi; $i++) if ($primes[$i]) $cnt++;
        return $r - $l + 1 - $cnt;
    }
}
