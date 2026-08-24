<?php
// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

class Solution {
    private function isPrime($x) {
        if ($x < 2) return false;
        $sqrtX = (int)sqrt($x);
        for ($i = 2; $i <= $sqrtX; $i++) if ($x % $i === 0) return false;
        return true;
    }

    function sumOfLargestPrimes($s) {
        $st = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $x = 0;
            for ($j = $i; $j < $n; $j++) {
                $x = $x * 10 + (ord($s[$j]) - 48);
                if ($this->isPrime($x)) $st[$x] = true;
            }
        }
        $nums = array_keys($st);
        sort($nums);
        $ans = 0;
        for ($i = count($nums) - 1; $i >= 0 && count($nums) - $i <= 3; $i--)
            $ans += $nums[$i];
        return $ans;
    }
}
