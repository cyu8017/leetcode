<?php
// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution {
    /**
     * @param Integer[] $days
     * @param Integer[] $costs
     * @return Integer
     */
    function mincostTickets($days, $costs) {
        $dayset = array_flip($days);
        $last = $days[count($days) - 1];
        $dp = array_fill(0, $last + 1, 0);
        for ($d = 1; $d <= $last; $d++) {
            if (!isset($dayset[$d])) $dp[$d] = $dp[$d - 1];
            else {
                $dp[$d] = min(
                    $dp[$d - 1] + $costs[0],
                    $dp[max(0, $d - 7)] + $costs[1],
                    $dp[max(0, $d - 30)] + $costs[2]
                );
            }
        }
        return $dp[$last];
    }
}
