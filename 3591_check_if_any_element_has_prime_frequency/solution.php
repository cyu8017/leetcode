<?php
// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

class Solution {
    private function isPrime($x) {
        if ($x < 2) return false;
        for ($i = 2; $i * $i <= $x; $i++) if ($x % $i === 0) return false;
        return true;
    }

    function checkPrimeFrequency($nums) {
        $cnt = [];
        foreach ($nums as $x) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        foreach ($cnt as $v) if ($this->isPrime($v)) return true;
        return false;
    }
}
