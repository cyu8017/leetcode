<?php
// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

class Solution {
    /**
     * @param Integer[][] $events
     * @param Integer $k
     * @return Integer
     */
    function maxValue($events, $k) {
        sort($events);
        $n = count($events);
        $starts = array_map(function ($e) { return $e[0]; }, $events);

        $upperBound = function ($target) use ($starts, $n) {
            $lo = 0;
            $hi = $n;
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($starts[$mid] <= $target) {
                    $lo = $mid + 1;
                } else {
                    $hi = $mid;
                }
            }
            return $lo;
        };

        $dp = array_fill(0, $k + 1, array_fill(0, $n + 1, 0));
        for ($i = $n - 1; $i >= 0; $i--) {
            $j = $upperBound($events[$i][1]);
            for ($remain = 1; $remain <= $k; $remain++) {
                $dp[$remain][$i] = max($dp[$remain][$i + 1], $events[$i][2] + $dp[$remain - 1][$j]);
            }
        }
        return $dp[$k][0];
    }
}
