<?php
// LeetCode 3980 - Minimum Operations to Transform Binary String
// https://leetcode.com/problems/minimum-operations-to-transform-binary-string/

class Solution {
    function minOperations($s1, $s2) {
        $infinity = 1000000000;
        $dp = [0, $infinity];
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) {
            $next = [$infinity, $infinity];
            for ($forcedZero = 0; $forcedZero <= 1; $forcedZero++) {
                if ($dp[$forcedZero] == $infinity) continue;
                $current = $s1[$i];
                if ($forcedZero == 1) $current = '0';
                $direct = $dp[$forcedZero];
                if ($current == '0' && $s2[$i] == '1') $direct++;
                else if ($current == '1' && $s2[$i] == '0') $direct = $infinity;
                $next[0] = min($next[0], $direct);
                if ($i + 1 < $n) {
                    $cost = $dp[$forcedZero] + 1;
                    if ($current == '0') $cost++;
                    if ($s1[$i + 1] == '0') $cost++;
                    if ($s2[$i] == '1') $cost++;
                    $next[1] = min($next[1], $cost);
                }
            }
            $dp = $next;
        }
        return $dp[0] == $infinity ? -1 : $dp[0];
    }
}
