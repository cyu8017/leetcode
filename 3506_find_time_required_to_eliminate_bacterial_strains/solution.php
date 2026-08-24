<?php
// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

class Solution {
    function minEliminationTime($timeReq, $splitTime) {
        $pq = $timeReq;
        sort($pq);
        $pq = array_values($pq);
        while (count($pq) > 1) {
            array_shift($pq);
            $x = array_shift($pq);
            $v = $x + $splitTime;
            $lo = 0;
            $hi = count($pq);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($pq[$mid] < $v) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($pq, $lo, 0, [$v]);
        }
        return $pq[0];
    }
}
