<?php
// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

class Solution {
    function numberOfWays($n, $x) {
        $MOD = 1000000007;
        $powers = [];
        for ($i = 1; ; $i++) {
            $p = 1;
            for ($j = 0; $j < $x; $j++) {
                $p *= $i;
                if ($p > $n) break;
            }
            if ($p > $n) break;
            $powers[] = $p;
        }
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        foreach ($powers as $p) {
            for ($s = $n; $s >= $p; $s--) $dp[$s] = ($dp[$s] + $dp[$s - $p]) % $MOD;
        }
        return $dp[$n];
    }
}
