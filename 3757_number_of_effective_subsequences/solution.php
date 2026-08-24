<?php
// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

class Solution {
    function countEffectiveSubsequences($nums) {
        $PopCount = function($x) {
            $c = 0;
            while ($x !== 0) { $c += $x & 1; $x >>= 1; }
            return $c;
        };
        $mod = 1000000007;
        $all = 0;
        foreach ($nums as $x) $all |= $x;
        $bits = [];
        for ($b = 0; $b < 20; $b++) if ((($all >> $b) & 1) !== 0) $bits[] = $b;
        $m = count($bits);
        $freq = array_fill(0, 1 << $m, 0);
        foreach ($nums as $x) {
            $mask = 0;
            for ($i = 0; $i < $m; $i++) if ((($x >> $bits[$i]) & 1) !== 0) $mask |= 1 << $i;
            $freq[$mask]++;
        }
        $disjoint = $freq;
        for ($b = 0; $b < $m; $b++) {
            for ($mask = 0; $mask < (1 << $m); $mask++) {
                if ((($mask >> $b) & 1) !== 0) $disjoint[$mask] += $disjoint[$mask ^ (1 << $b)];
            }
        }
        $pow2 = array_fill(0, count($nums) + 1, 0);
        $pow2[0] = 1;
        for ($i = 1; $i <= count($nums); $i++) $pow2[$i] = $pow2[$i - 1] * 2 % $mod;
        $ans = 0;
        $full = (1 << $m) - 1;
        for ($s = 1; $s <= $full; $s++) {
            $ways = $pow2[$disjoint[$full ^ $s]];
            $bc = $PopCount($s);
            if (($bc & 1) !== 0) {
                $ans += $ways;
                if ($ans >= $mod) $ans -= $mod;
            } else {
                $ans -= $ways;
                if ($ans < 0) $ans += $mod;
            }
        }
        return $ans;
    }
}
