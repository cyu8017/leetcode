<?php
// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

class Solution {
    function minOperations($nums, $numsDivide) {
        $g = $numsDivide[0];
        $nd = count($numsDivide);
        for ($i = 1; $i < $nd; $i++) $g = $this->gcd($g, $numsDivide[$i]);
        sort($nums);
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($g % $nums[$i] === 0) return $i;
        }
        return -1;
    }

    private function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }
}
