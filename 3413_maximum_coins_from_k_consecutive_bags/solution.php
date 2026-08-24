<?php
// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

class Solution {
    function maximumCoins($coins, $k) {
        usort($coins, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = 0;
        $n = count($coins);
        for ($i = 0; $i < $n; $i++) {
            $sum = 0;
            $start = $coins[$i][0];
            $end = $start + $k - 1;
            for ($j = $i; $j < $n && $coins[$j][0] <= $end; $j++) {
                $l = $coins[$j][0];
                $r = $coins[$j][1];
                if ($r > $end) $r = $end;
                if ($l < $start) $l = $start;
                if ($l <= $r) $sum += ($r - $l + 1) * $coins[$j][2];
            }
            if ($sum > $ans) $ans = $sum;
        }
        for ($i = 0; $i < $n; $i++) {
            $sum = 0;
            $end = $coins[$i][1];
            $start = $end - $k + 1;
            for ($j = 0; $j <= $i; $j++) {
                $l = $coins[$j][0];
                $r = $coins[$j][1];
                if ($l < $start) $l = $start;
                if ($r > $end) $r = $end;
                if ($l <= $r) $sum += ($r - $l + 1) * $coins[$j][2];
            }
            if ($sum > $ans) $ans = $sum;
        }
        return $ans;
    }
}
