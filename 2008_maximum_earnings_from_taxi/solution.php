<?php
// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $rides
     * @return Integer
     */
    function maxTaxiEarnings($n, $rides) {
        usort($rides, fn($a, $b) => $a[1] <=> $b[1]);
        $m = count($rides);
        $ends = array_map(fn($r) => $r[1], $rides);
        $dp = array_fill(0, $m + 1, 0);
        for ($i = 0; $i < $m; $i++) {
            [$start, $end, $tip] = $rides[$i];
            $earn = $end - $start + $tip;
            $lo = 0;
            $hi = $m;
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($ends[$mid] <= $start) $lo = $mid + 1;
                else $hi = $mid;
            }
            $dp[$i + 1] = max($dp[$i], $earn + $dp[$lo]);
        }
        return $dp[$m];
    }
}
