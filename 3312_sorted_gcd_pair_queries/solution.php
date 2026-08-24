<?php
// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

class Solution {
    function gcdValues($nums, $queries) {
        $maxV = 0;
        foreach ($nums as $x) if ($x > $maxV) $maxV = $x;
        $cnt = array_fill(0, $maxV + 1, 0);
        foreach ($nums as $x) $cnt[$x]++;
        $divCnt = array_fill(0, $maxV + 1, 0);
        for ($g = 1; $g <= $maxV; $g++) {
            $c = 0;
            for ($m = $g; $m <= $maxV; $m += $g) $c += $cnt[$m];
            $divCnt[$g] = $c * ($c - 1) / 2;
        }
        $exact = array_fill(0, $maxV + 1, 0);
        for ($g = $maxV; $g >= 1; $g--) {
            $exact[$g] = $divCnt[$g];
            for ($m = 2 * $g; $m <= $maxV; $m += $g) $exact[$g] -= $exact[$m];
        }
        $pref = array_fill(0, $maxV + 1, 0);
        for ($g = 1; $g <= $maxV; $g++) $pref[$g] = $pref[$g - 1] + $exact[$g];
        $ans = [];
        $qn = count($queries);
        for ($i = 0; $i < $qn; $i++) {
            $q = $queries[$i];
            $lo = 1;
            $hi = $maxV;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($pref[$mid] > $q) $hi = $mid;
                else $lo = $mid + 1;
            }
            $ans[$i] = $lo;
        }
        return $ans;
    }
}
