<?php
// LeetCode 3896 - Minimum Operations to Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

class Solution {
    static $isPrime = null;
    static $primes = null;
    const MX = 200000;
    function init() {
        if (self::$isPrime !== null) return;
        self::$isPrime = array_fill(0, self::MX + 1, true);
        self::$isPrime[0] = self::$isPrime[1] = false;
        for ($i = 2; $i * $i <= self::MX; $i++) {
            if (self::$isPrime[$i]) {
                for ($j = $i * $i; $j <= self::MX; $j += $i) self::$isPrime[$j] = false;
            }
        }
        self::$primes = [];
        for ($i = 2; $i <= self::MX; $i++) if (self::$isPrime[$i]) self::$primes[] = $i;
    }
    function minOperations($nums) {
        $this->init();
        $ans = 0;
        $n = count($nums);
        $pn = count(self::$primes);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            if ($i % 2 === 0) {
                $lo = 0;
                $hi = $pn;
                while ($lo < $hi) {
                    $mid = ($lo + $hi) >> 1;
                    if (self::$primes[$mid] < $x) $lo = $mid + 1;
                    else $hi = $mid;
                }
                $ans += self::$primes[$lo] - $x;
            } else if (self::$isPrime[$x]) {
                $ans += ($x === 2) ? 2 : 1;
            }
        }
        return $ans;
    }
}
