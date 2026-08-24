<?php
// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

class Solution {
    /**
     * @param Integer[][] $tires
     * @param Integer $changeTime
     * @param Integer $numLaps
     * @return Integer
     */
    function minimumFinishTime($tires, $changeTime, $numLaps) {
        $INF = 1 << 30;
        $minTime = array_fill(0, 20, $INF);
        foreach ($tires as $tire) {
            $f = $tire[0];
            $r = $tire[1];
            $t = $f;
            $lap = $f;
            for ($x = 1; $x < 20 && $t < $minTime[$x]; $x++) {
                $minTime[$x] = $t;
                $lap *= $r;
                if ($lap > $changeTime + $f) break;
                $t += $lap;
            }
        }
        $dp = array_fill(0, $numLaps + 1, $INF);
        $dp[0] = -$changeTime;
        for ($i = 1; $i <= $numLaps; $i++)
            for ($j = 1; $j <= $i && $j < 20; $j++)
                $dp[$i] = min($dp[$i], $dp[$i - $j] + $changeTime + $minTime[$j]);
        return $dp[$numLaps];
    }
}
