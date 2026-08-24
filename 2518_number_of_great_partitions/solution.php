<?php
// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

class Solution {
    function countPartitions($nums, $k) {
        $MOD = 1000000007;
        $sum = 0;
        foreach ($nums as $x) $sum += $x;
        if ($sum < 2 * $k) return 0;
        $dp = array_fill(0, $k, 0);
        $dp[0] = 1;
        foreach ($nums as $x) {
            for ($s = $k - 1; $s >= $x; $s--)
                $dp[$s] = ($dp[$s] + $dp[$s - $x]) % $MOD;
        }
        $bad = 0;
        foreach ($dp as $v) $bad = ($bad + $v) % $MOD;
        $total = 1;
        for ($i = 0; $i < count($nums); $i++) $total = ($total * 2) % $MOD;
        return ($total - (2 * $bad) % $MOD + $MOD) % $MOD;
    }
}
