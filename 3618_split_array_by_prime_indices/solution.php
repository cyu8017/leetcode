<?php
// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

class Solution {
    private static $primes = null;

    function splitArray($nums) {
        $M = 100010;
        if (self::$primes === null) {
            $primes = array_fill(0, $M, true);
            $primes[0] = $primes[1] = false;
            for ($i = 2; $i < $M; $i++)
                if ($primes[$i])
                    for ($j = $i + $i; $j < $M; $j += $i) $primes[$j] = false;
            self::$primes = $primes;
        }
        $pr = self::$primes;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($pr[$i]) $ans += $nums[$i];
            else $ans -= $nums[$i];
        }
        return abs($ans);
    }
}
