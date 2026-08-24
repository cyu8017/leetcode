<?php
// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

class Solution {
    function countPairs($coordinates, $k) {
        $freq = [];
        $ans = 0;
        foreach ($coordinates as $xy) {
            $x = $xy[0];
            $y = $xy[1];
            for ($a = 0; $a <= $k; $a++) {
                $b = $k - $a;
                $key = ($x ^ $a) . ',' . ($y ^ $b);
                $ans += $freq[$key] ?? 0;
            }
            $k0 = $x . ',' . $y;
            if (!isset($freq[$k0])) $freq[$k0] = 0;
            $freq[$k0]++;
        }
        return $ans;
    }
}
