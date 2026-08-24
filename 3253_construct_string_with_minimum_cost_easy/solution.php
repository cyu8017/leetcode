<?php
// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

class Solution {
    function minimumCost($target, $words, $costs) {
        $inf = 1e18;
        $n = strlen($target);
        $dp = array_fill(0, $n + 1, $inf);
        $dp[0] = 0;
        $best = [];
        for ($i = 0; $i < count($words); $i++) {
            $old = $best[$words[$i]] ?? null;
            if ($old === null || $costs[$i] < $old) $best[$words[$i]] = $costs[$i];
        }
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] === $inf) continue;
            foreach ($best as $w => $c) {
                $L = strlen($w);
                if ($i + $L <= $n && substr($target, $i, $L) === $w && $dp[$i] + $c < $dp[$i + $L]) $dp[$i + $L] = $dp[$i] + $c;
            }
        }
        if ($dp[$n] === $inf) return -1;
        return $dp[$n];
    }
}
