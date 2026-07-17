<?php
// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

class Solution {
    /**
     * @param Integer[] $dist
     * @param Integer $speed
     * @param Integer $hoursBefore
     * @return Integer
     */
    function minSkips($dist, $speed, $hoursBefore) {
        $limit = $hoursBefore * $speed;
        $n = count($dist);
        $dp = array_fill(0, $n + 1, PHP_INT_MAX);
        $dp[0] = 0;

        foreach ($dist as $road) {
            $nxt = array_fill(0, $n + 1, PHP_INT_MAX);
            for ($skips = 0; $skips < $n; $skips++) {
                if ($dp[$skips] === PHP_INT_MAX) {
                    continue;
                }
                $nxt[$skips] = min(
                    $nxt[$skips],
                    intdiv($dp[$skips] + $road + $speed - 1, $speed) * $speed
                );
                $nxt[$skips + 1] = min($nxt[$skips + 1], $dp[$skips] + $road);
            }
            $dp = $nxt;
        }

        foreach ($dp as $skips => $total) {
            if ($total <= $limit) {
                return $skips;
            }
        }
        return -1;
    }
}
