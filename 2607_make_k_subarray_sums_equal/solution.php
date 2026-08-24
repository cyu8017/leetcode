<?php
// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

class Solution {
    function makeSubKSumEqual($arr, $k) {
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $n = count($arr);
        $g = $gcd($n, $k);
        $ans = 0;
        for ($r = 0; $r < $g; $r++) {
            $group = [];
            for ($i = $r; $i < $n; $i += $g) $group[] = $arr[$i];
            sort($group);
            $med = $group[intdiv(count($group), 2)];
            foreach ($group as $x) $ans += abs($x - $med);
        }
        return $ans;
    }
}
