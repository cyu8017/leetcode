<?php
// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

class Solution {
    function minimumTime($power) {
        $n = count($power);
        $N = 1 << $n;
        $inf = intdiv(PHP_INT_MAX, 4);
        $dp = array_fill(0, $N, $inf);
        $dp[0] = 0;
        for ($mask = 0; $mask < $N; $mask++) {
            $killed = $this->bitCount($mask);
            $gain = $killed + 1;
            for ($i = 0; $i < $n; $i++) {
                if (($mask & (1 << $i)) !== 0) continue;
                $need = intdiv($power[$i] + $gain - 1, $gain);
                $nm = $mask | (1 << $i);
                $dp[$nm] = min($dp[$nm], $dp[$mask] + $need);
            }
        }
        return $dp[$N - 1];
    }

    private function bitCount($x) {
        $c = 0;
        while ($x !== 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }
}
