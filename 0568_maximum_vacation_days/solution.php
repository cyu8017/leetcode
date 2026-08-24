<?php
// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

class Solution {
    function maxVacationDays($flights, $days) {
        $cities = count($flights);
        $weeks = count($days[0]);
        $NEG = -1000000000;
        $dp = array_fill(0, $cities, $NEG);
        $dp[0] = 0;
        for ($week = 0; $week < $weeks; ++$week) {
            $nxt = array_fill(0, $cities, $NEG);
            for ($city = 0; $city < $cities; ++$city) {
                if ($dp[$city] === $NEG) continue;
                for ($dest = 0; $dest < $cities; ++$dest) {
                    if ($dest === $city || $flights[$city][$dest] === 1) {
                        $nxt[$dest] = max($nxt[$dest], $dp[$city] + $days[$dest][$week]);
                    }
                }
            }
            $dp = $nxt;
        }
        $best = $NEG;
        foreach ($dp as $v) $best = max($best, $v);
        return $best;
    }
}
