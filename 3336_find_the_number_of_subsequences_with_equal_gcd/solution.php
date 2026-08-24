<?php
// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

class Solution {
    function gcd($a, $b) {
        if ($a === 0) return $b;
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    function subsequencePairCount($nums) {
        $mod = 1000000007;
        $maxV = 0;
        foreach ($nums as $x) if ($x > $maxV) $maxV = $x;
        $dp = [];
        for ($a = 0; $a <= $maxV; $a++) $dp[$a] = array_fill(0, $maxV + 1, 0);
        $dp[0][0] = 1;
        foreach ($nums as $x) {
            $ndp = [];
            for ($a = 0; $a <= $maxV; $a++) {
                $ndp[$a] = [];
                for ($b = 0; $b <= $maxV; $b++) $ndp[$a][$b] = $dp[$a][$b];
            }
            for ($a = 0; $a <= $maxV; $a++) {
                for ($b = 0; $b <= $maxV; $b++) {
                    if ($dp[$a][$b] === 0) continue;
                    $na = $a === 0 ? $x : $this->gcd($a, $x);
                    $nb = $b === 0 ? $x : $this->gcd($b, $x);
                    $ndp[$na][$b] = ($ndp[$na][$b] + $dp[$a][$b]) % $mod;
                    $ndp[$a][$nb] = ($ndp[$a][$nb] + $dp[$a][$b]) % $mod;
                }
            }
            $dp = $ndp;
        }
        $ans = 0;
        for ($g = 1; $g <= $maxV; $g++) $ans = ($ans + $dp[$g][$g]) % $mod;
        return $ans;
    }
}
