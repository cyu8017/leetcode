<?php
// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

class Solution {
    private function entry($i, $j) {
        return ($i + 1) * ($j + 1);
    }

    function minCost($m, $n, $waitCost) {
        $INF = PHP_INT_MAX >> 2;
        $dp = [];
        for ($i = 0; $i < $m; $i++) $dp[$i] = array_fill(0, $n, $INF);
        $dp[0][0] = $this->entry(0, 0);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i === 0 && $j === 0) continue;
                if ($i > 0) {
                    $cand = $dp[$i - 1][$j] + $this->entry($i, $j);
                    if (!($i - 1 === 0 && $j === 0)) $cand += $waitCost[$i - 1][$j];
                    $dp[$i][$j] = min($dp[$i][$j], $cand);
                }
                if ($j > 0) {
                    $cand = $dp[$i][$j - 1] + $this->entry($i, $j);
                    if (!($i === 0 && $j - 1 === 0)) $cand += $waitCost[$i][$j - 1];
                    $dp[$i][$j] = min($dp[$i][$j], $cand);
                }
            }
        }
        return $dp[$m - 1][$n - 1];
    }
}
