<?php
// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

class Solution {
    function findPrimePairs($n) {
        $isPrime = array_fill(0, $n + 1, true);
        $isPrime[0] = $isPrime[1] = false;
        for ($i = 2; $i * $i <= $n; $i++) {
            if ($isPrime[$i]) {
                for ($j = $i * $i; $j <= $n; $j += $i) $isPrime[$j] = false;
            }
        }
        $ans = [];
        for ($x = 2; $x <= intdiv($n, 2); $x++) {
            $y = $n - $x;
            if ($isPrime[$x] && $isPrime[$y]) $ans[] = [$x, $y];
        }
        return $ans;
    }
}
