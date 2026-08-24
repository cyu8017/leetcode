<?php
// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

class Solution {
    function strangePrinter($s) {
        $n = strlen($s);
        if ($n === 0) return 0;
        $dp = [];
        for ($i = 0; $i < $n; ++$i) $dp[$i] = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; --$i) {
            $dp[$i][$i] = 1;
            for ($j = $i + 1; $j < $n; ++$j) {
                $dp[$i][$j] = $dp[$i + 1][$j] + 1;
                for ($k = $i + 1; $k <= $j; ++$k) {
                    if ($s[$k] === $s[$i]) {
                        $dp[$i][$j] = min($dp[$i][$j], $dp[$i][$k - 1] + ($k + 1 <= $j ? $dp[$k + 1][$j] : 0));
                    }
                }
            }
        }
        return $dp[0][$n - 1];
    }
}
