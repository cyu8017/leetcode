<?php
// LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

class Solution {
    function countCoprime($mat) {
        $MOD = 1000000007;
        $m = count($mat);
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $dp = [];
        foreach ($mat[0] as $v) {
            if (!isset($dp[$v])) $dp[$v] = 0;
            $dp[$v]++;
        }
        for ($i = 1; $i < $m; $i++) {
            $ndp = [];
            foreach ($mat[$i] as $v) {
                foreach ($dp as $key => $val) {
                    $ng = $gcd($key, $v);
                    if (!isset($ndp[$ng])) $ndp[$ng] = 0;
                    $ndp[$ng] = ($ndp[$ng] + $val) % $MOD;
                }
            }
            $dp = $ndp;
        }
        return isset($dp[1]) ? $dp[1] : 0;
    }
}
