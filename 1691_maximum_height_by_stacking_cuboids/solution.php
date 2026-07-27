<?php
// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

class Solution {
    function maxHeight($cuboids) {
        $a = [];
        foreach ($cuboids as $c) {
            sort($c);
            $a[] = $c;
        }
        usort($a, function($x, $y) {
            return $x <=> $y;
        });
        $n = count($a);
        $dp = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $dp[$i] = $a[$i][2];
            for ($j = 0; $j < $i; $j++) {
                if ($a[$j][0] <= $a[$i][0] && $a[$j][1] <= $a[$i][1] && $a[$j][2] <= $a[$i][2]) {
                    $dp[$i] = max($dp[$i], $dp[$j] + $a[$i][2]);
                }
            }
        }
        return max($dp);
    }
}
