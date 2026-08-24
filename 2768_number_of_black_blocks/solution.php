<?php
// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

class Solution {
    function countBlackBlocks($m, $n, $coordinates) {
        $cnt = [];
        foreach ($coordinates as $c) {
            $x = $c[0];
            $y = $c[1];
            for ($i = $x - 1; $i <= $x; $i++) {
                for ($j = $y - 1; $j <= $y; $j++) {
                    if ($i >= 0 && $j >= 0 && $i < $m - 1 && $j < $n - 1) {
                        $key = $i . ',' . $j;
                        $cnt[$key] = ($cnt[$key] ?? 0) + 1;
                    }
                }
            }
        }
        $out = array_fill(0, 5, 0);
        $out[0] = ($m - 1) * ($n - 1);
        foreach ($cnt as $v) {
            $out[$v]++;
            $out[0]--;
        }
        return $out;
    }
}
