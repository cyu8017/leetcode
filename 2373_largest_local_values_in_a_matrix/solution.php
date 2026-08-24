<?php
// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution {
    function largestLocal($grid) {
        $n = count($grid);
        $ans = array_fill(0, $n - 2, array_fill(0, $n - 2, 0));
        for ($i = 0; $i < $n - 2; $i++) {
            for ($j = 0; $j < $n - 2; $j++) {
                $mx = 0;
                for ($r = $i; $r < $i + 3; $r++)
                    for ($c = $j; $c < $j + 3; $c++)
                        if ($grid[$r][$c] > $mx) $mx = $grid[$r][$c];
                $ans[$i][$j] = $mx;
            }
        }
        return $ans;
    }
}
