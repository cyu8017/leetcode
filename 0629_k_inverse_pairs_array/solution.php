<?php
// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

class Solution {
    function kInversePairs($n, $k) {
        $mod = 1000000007;
        $dp = array_fill(0, $k + 1, 0);
        $dp[0] = 1;
        for ($size = 1; $size <= $n; ++$size) {
            $nxt = array_fill(0, $k + 1, 0);
            $prefix = 0;
            for ($pairs = 0; $pairs <= $k; ++$pairs) {
                $prefix = ($prefix + $dp[$pairs]) % $mod;
                if ($pairs >= $size) $prefix = ($prefix - $dp[$pairs - $size] + $mod) % $mod;
                $nxt[$pairs] = $prefix;
            }
            $dp = $nxt;
        }
        return $dp[$k];
    }
}
