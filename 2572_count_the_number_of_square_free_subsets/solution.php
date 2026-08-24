<?php
// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

class Solution {
    function squareFreeSubsets($nums) {
        $MOD = 1000000007;
        $PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        $freq = [];
        foreach ($nums as $x) $freq[$x] = ($freq[$x] ?? 0) + 1;
        $maskOf = function($x) use ($PRIMES) {
            $mask = 0;
            for ($i = 0; $i < count($PRIMES); $i++) {
                $p = $PRIMES[$i];
                $cnt = 0;
                while ($x % $p === 0) {
                    $x = intdiv($x, $p);
                    $cnt++;
                    if ($cnt > 1) return -1;
                }
                if ($cnt === 1) $mask |= 1 << $i;
            }
            return $mask;
        };
        $dp = array_fill(0, 1 << 10, 0);
        $dp[0] = 1;
        foreach ($freq as $x => $c) {
            if ($x === 1) continue;
            $m = $maskOf($x);
            if ($m < 0) continue;
            for ($state = (1 << 10) - 1; $state >= 0; $state--) {
                if (($state & $m) === 0) {
                    $dp[$state | $m] = ($dp[$state | $m] + $dp[$state] * $c) % $MOD;
                }
            }
        }
        $ans = 0;
        foreach ($dp as $v) $ans = ($ans + $v) % $MOD;
        $ones = $freq[1] ?? 0;
        $mul = 1;
        for ($i = 0; $i < $ones; $i++) $mul = $mul * 2 % $MOD;
        $ans = $ans * $mul % $MOD;
        $ans = ($ans - 1 + $MOD) % $MOD;
        return $ans;
    }
}
