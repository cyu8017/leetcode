<?php
// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

class Solution {
    function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    function lcm($a, $b) {
        return intdiv($a, $this->gcd($a, $b)) * $b;
    }

    function maxScore($nums) {
        $n = count($nums);
        $gcdAll = $nums[0];
        $lcmAll = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            $gcdAll = $this->gcd($gcdAll, $nums[$i]);
            $lcmAll = $this->lcm($lcmAll, $nums[$i]);
        }
        $ans = $gcdAll * $lcmAll;
        for ($skip = 0; $skip < $n; $skip++) {
            $g = 0;
            $l = 1;
            $first = true;
            for ($i = 0; $i < $n; $i++) {
                if ($i === $skip) continue;
                if ($first) { $g = $l = $nums[$i]; $first = false; }
                else { $g = $this->gcd($g, $nums[$i]); $l = $this->lcm($l, $nums[$i]); }
            }
            if ($first) continue;
            $v = $g * $l;
            if ($v > $ans) $ans = $v;
        }
        return $ans;
    }
}
