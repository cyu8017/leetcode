<?php
// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

class Solution {
    /**
     * @param Integer[][] $customers
     * @return Float
     */
    function averageWaitingTime($customers) {
        $current = 0;
        $total = 0;
        foreach ($customers as [$arrival, $cook]) {
            $current = max($current, $arrival) + $cook;
            $total += $current - $arrival;
        }
        return $total / count($customers);
    }
}
