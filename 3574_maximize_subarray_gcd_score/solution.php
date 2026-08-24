<?php
// LeetCode 3574 - Maximize Subarray GCD Score
// https://leetcode.com/problems/maximize-subarray-gcd-score/

class Solution {
    private function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    function maxGCDScore($nums, $k) {
        $n = count($nums);
        $cnt = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            while ($x % 2 === 0) { $cnt[$i]++; $x = intdiv($x, 2); }
        }
        $ans = 0;
        for ($l = 0; $l < $n; $l++) {
            $g = 0;
            $mi = 2147483647;
            $t = 0;
            for ($r = $l; $r < $n; $r++) {
                $g = $this->gcd($g, $nums[$r]);
                if ($cnt[$r] < $mi) { $mi = $cnt[$r]; $t = 1; }
                else if ($cnt[$r] === $mi) $t++;
                $score = $g * ($r - $l + 1);
                if ($t <= $k) $score *= 2;
                $ans = max($ans, $score);
            }
        }
        return $ans;
    }
}
