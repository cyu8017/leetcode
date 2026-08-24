<?php
// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

class Solution {
    function filterOccupiedIntervals($occupiedIntervals, $freeStart, $freeEnd) {
        usort($occupiedIntervals, function ($a, $b) { return $a[0] <=> $b[0]; });
        $busy = [[$occupiedIntervals[0][0], $occupiedIntervals[0][1]]];
        for ($i = 1; $i < count($occupiedIntervals); $i++) {
            $cur = $occupiedIntervals[$i];
            $last = count($busy) - 1;
            if ($busy[$last][1] + 1 < $cur[0]) $busy[] = [$cur[0], $cur[1]];
            else if ($cur[1] > $busy[$last][1]) $busy[$last][1] = $cur[1];
        }
        $ans = [];
        foreach ($busy as $it) {
            $s = $it[0];
            $e = $it[1];
            if ($e < $freeStart || $s > $freeEnd) $ans[] = [$s, $e];
            else {
                if ($s < $freeStart) $ans[] = [$s, $freeStart - 1];
                if ($e > $freeEnd) $ans[] = [$freeEnd + 1, $e];
            }
        }
        return $ans;
    }
}
