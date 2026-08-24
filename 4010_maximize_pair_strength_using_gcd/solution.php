<?php
// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/

class Solution {
    function maxPairStrength($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $g = $this->gcd($nums[$i], $nums[$j]);
                $x = intdiv($nums[$i] * $nums[$j], $g * $g);
                $ans = max($ans, $x);
            }
        }
        return $ans;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
}
