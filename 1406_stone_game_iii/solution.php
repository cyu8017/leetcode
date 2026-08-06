<?php
class Solution {
    function stoneGameIII($stoneValue) {
        $n = count($stoneValue);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $take = 0;
            $dp[$i] = -10 ** 18;
            for ($j = $i; $j < min($i + 3, $n); $j++) {
                $take += $stoneValue[$j];
                $dp[$i] = max($dp[$i], $take - $dp[$j + 1]);
            }
        }
        if ($dp[0] > 0) return "Alice";
        if ($dp[0] < 0) return "Bob";
        return "Tie";
    }
}
