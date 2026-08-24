<?php
// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

class Solution {
    function distinctSubseqII($s) {
        $MOD = 1000000007;
        $last = array_fill(0, 26, -1);
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        for ($i = 0; $i < $n; $i++) {
            $c = ord($s[$i]) - 97;
            $dp[$i + 1] = ($dp[$i] * 2) % $MOD;
            if ($last[$c] >= 0) $dp[$i + 1] = ($dp[$i + 1] - $dp[$last[$c]] + $MOD) % $MOD;
            $last[$c] = $i;
        }
        return ($dp[$n] - 1 + $MOD) % $MOD;
    }
}
