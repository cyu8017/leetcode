<?php
// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

class Solution {
    function maxHammingDistances($nums, $m) {
        $dist = array_fill(0, 1 << $m, -1);
        $q = [];
        foreach ($nums as $x) {
            $dist[$x] = 0;
            $q[] = $x;
        }
        for ($k = 1; $q; $k++) {
            $t = [];
            foreach ($q as $x) {
                for ($i = 0; $i < $m; $i++) {
                    $y = $x ^ (1 << $i);
                    if ($dist[$y] === -1) {
                        $dist[$y] = $k;
                        $t[] = $y;
                    }
                }
            }
            $q = $t;
        }
        $ans = $nums;
        $mask = (1 << $m) - 1;
        for ($i = 0; $i < count($ans); $i++) {
            $x = $ans[$i];
            $ans[$i] = $m - $dist[$x ^ $mask];
        }
        return $ans;
    }
}
