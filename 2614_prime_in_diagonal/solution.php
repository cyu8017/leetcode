<?php
// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

class Solution {
    function diagonalPrime($nums) {
        $isPrime = function($x) {
            if ($x < 2) return false;
            for ($i = 2; $i * $i <= $x; $i++) if ($x % $i === 0) return false;
            return true;
        };
        $n = count($nums);
        $best = 0;
        for ($i = 0; $i < $n; $i++) {
            $a = $nums[$i][$i];
            $b = $nums[$i][$n - 1 - $i];
            if ($isPrime($a) && $a > $best) $best = $a;
            if ($isPrime($b) && $b > $best) $best = $b;
        }
        return $best;
    }
}
