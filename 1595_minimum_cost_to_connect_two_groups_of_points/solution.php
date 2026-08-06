<?php

class Solution {
    /**
     * @param Integer[][] $cost
     * @return Integer
     */
    function connectTwoGroups($cost) {
        $m = count($cost);
        $n = count($cost[0]);
        $full = 1 << $n;
        $inf = 1000000000;
        $dp = array_fill(0, $full, $inf);
        $dp[0] = 0;

        foreach ($cost as $row) {
            $nxt = array_fill(0, $full, $inf);
            for ($mask = 0; $mask < $full; $mask++) {
                for ($j = 0; $j < $n; $j++) {
                    $newMask = $mask | (1 << $j);
                    $nxt[$newMask] = min($nxt[$newMask], $dp[$mask] + $row[$j], $nxt[$mask] + $row[$j]);
                }
            }
            $dp = $nxt;
        }

        $minimum = [];
        for ($j = 0; $j < $n; $j++) {
            $mn = $inf;
            for ($i = 0; $i < $m; $i++) {
                $mn = min($mn, $cost[$i][$j]);
            }
            $minimum[$j] = $mn;
        }

        $answer = $inf;
        for ($mask = 0; $mask < $full; $mask++) {
            $extra = 0;
            for ($j = 0; $j < $n; $j++) {
                if ((($mask >> $j) & 1) === 0) {
                    $extra += $minimum[$j];
                }
            }
            $answer = min($answer, $dp[$mask] + $extra);
        }
        return $answer;
    }
}
