<?php
// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

class Solution {
    function maximumPrimeDifference($nums) {
        for ($i = 0; ; $i++) {
            if ($this->isPrime($nums[$i])) {
                for ($j = count($nums) - 1; ; $j--) {
                    if ($this->isPrime($nums[$j])) return $j - $i;
                }
            }
        }
    }
    function isPrime($n) {
        if ($n < 2) return false;
        for ($i = 2; $i * $i <= $n; $i++) if ($n % $i === 0) return false;
        return true;
    }
}
