<?php
// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

class Solution {
    function bitsOnes($x) {
        $c = 0;
        while ($x > 0) { $c += $x & 1; $x >>= 1; }
        return $c;
    }

    function findMinimumTime($strength, $k) {
        $n = count($strength);
        $inf = 1000000000;
        $N = 1 << $n;
        $dp = array_fill(0, $N, $inf);
        $dp[0] = 0;
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
