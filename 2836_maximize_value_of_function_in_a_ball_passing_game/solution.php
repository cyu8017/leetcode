<?php
// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

class Solution {
    function getMaxFunctionValue($receiver, $k) {
        $n = count($receiver);
        $LOG = 36;
        $up = [];
        $sum = [];
        for ($j = 0; $j < $LOG; $j++) {
            $up[$j] = array_fill(0, $n, 0);
            $sum[$j] = array_fill(0, $n, 0);
        }
        for ($i = 0; $i < $n; $i++) {
            $up[0][$i] = $receiver[$i];
            $sum[0][$i] = $receiver[$i];
        }
        for ($j = 1; $j < $LOG; $j++) {
            for ($i = 0; $i < $n; $i++) {
                $mid = $up[$j - 1][$i];
                $up[$j][$i] = $up[$j - 1][$mid];
                $sum[$j][$i] = $sum[$j - 1][$i] + $sum[$j - 1][$mid];
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cur = $i;
            $total = $i;
            $kk = $k;
            for ($j = 0; $j < $LOG; $j++) {
                if (($kk & (1 << $j)) !== 0) {
                    $total += $sum[$j][$cur];
                    $cur = $up[$j][$cur];
                }
            }
            if ($total > $ans) $ans = $total;
        }
        return $ans;
    }
}
