<?php
// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

class Solution {
    function cheapestJump($coins, $maxJump) {
        $n = count($coins);
        if ($coins[$n - 1] === -1) return [];
        $inf = intdiv(PHP_INT_MAX, 4);
        $cost = array_fill(0, $n, $inf);
        $nxt = array_fill(0, $n, -1);
        $cost[$n - 1] = $coins[$n - 1];
        for ($i = $n - 2; $i >= 0; --$i) {
            if ($coins[$i] === -1) continue;
            for ($jump = 1; $jump <= $maxJump; ++$jump) {
                $j = $i + $jump;
                if ($j >= $n) break;
                if ($cost[$j] === $inf) continue;
                $candidate = $coins[$i] + $cost[$j];
                if ($candidate < $cost[$i] || ($candidate === $cost[$i] && ($nxt[$i] === -1 || $j < $nxt[$i]))) {
                    $cost[$i] = $candidate;
                    $nxt[$i] = $j;
                }
            }
        }
        if ($cost[0] === $inf) return [];
        $path = [1];
        $i = 0;
        while ($i !== $n - 1) {
            $i = $nxt[$i];
            $path[] = $i + 1;
        }
        return $path;
    }
}
