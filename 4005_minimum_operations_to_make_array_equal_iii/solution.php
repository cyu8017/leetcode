<?php
// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

class Solution {
    function minOperations($nums) {
        $n = count($nums);
        if ($n <= 1) return 0;
        $g = $nums[0];
        $mn = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            $g = $this->gcd($g, $nums[$i]);
            $mn = min($mn, $nums[$i]);
        }
        $cands = [];
        foreach ($nums as $x) $cands[$x] = true;
        for ($d = 1; $d * $d <= $mn; $d++) {
            if ($mn % $d == 0) {
                $cands[$d] = true;
                $cands[intdiv($mn, $d)] = true;
            }
        }
        $cands[$g] = true;
        $ans = 2147483647;
        foreach ($cands as $t => $_) {
            $sum = 0;
            foreach ($nums as $x) {
                $sum += $this->cost($x, $t);
                if ($sum >= $ans) break;
            }
            $ans = min($ans, $sum);
        }
        return $ans;
    }

    private function cost($x, $t) {
        if ($x == $t) return 0;
        if ($x % $t == 0 || $t % $x == 0) return 1;
        return 2;
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
