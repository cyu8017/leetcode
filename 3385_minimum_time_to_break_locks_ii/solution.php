<?php
// LeetCode 3385 - Minimum Time to Break Locks II
// https://leetcode.com/problems/minimum-time-to-break-locks-ii/

class Solution {
    function bitsOnes($x) {
        $c = 0;
        while ($x > 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function findMinimumTime($strength) {
        $n = count($strength);
        $N = 1 << $n;
        $inf = 1e18;
        $dp = array_fill(0, $N, $inf);
        $dp[0] = 0;
        $k = 1;
        for ($mask = 0; $mask < $N; $mask++) {
            if ($dp[$mask] === $inf) continue;
            $opened = $this->bitsOnes($mask);
            $x = 1 + $opened * $k;
            for ($i = 0; $i < $n; $i++) {
                if (($mask & (1 << $i)) !== 0) continue;
                $t = intdiv($strength[$i] + $x - 1, $x);
                $nmask = $mask | (1 << $i);
                if ($dp[$mask] + $t < $dp[$nmask]) $dp[$nmask] = $dp[$mask] + $t;
            }
        }
        return $dp[$N - 1];
    }
}
