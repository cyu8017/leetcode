<?php
// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

class Solution {
    function minimumBeautifulSubstrings($s) {
        $n = strlen($s);
        $pow5 = [];
        $x = 1;
        while (true) {
            $b = decbin($x);
            if (strlen($b) > $n) break;
            $pow5[$b] = true;
            $x *= 5;
        }
        $INF = 1000000000;
        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] === $INF || $s[$i] === '0') continue;
            for ($j = $i + 1; $j <= $n; $j++) {
                $sub = substr($s, $i, $j - $i);
                if (isset($pow5[$sub])) $dp[$j] = min($dp[$j], $dp[$i] + 1);
            }
        }
        return $dp[$n] === $INF ? -1 : $dp[$n];
    }
}
