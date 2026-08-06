<?php
// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

class Solution {
    /**
     * @param Integer[][] $intervals
     * @param Integer[] $toBeRemoved
     * @return Integer[][]
     */
    function removeInterval($intervals, $toBeRemoved) {
        [$left, $right] = $toBeRemoved;
        $answer = [];
        foreach ($intervals as [$start, $end]) {
            if ($end <= $left || $start >= $right) {
                $answer[] = [$start, $end];
            } else {
                if ($start < $left) $answer[] = [$start, $left];
                if ($end > $right) $answer[] = [$right, $end];
            }
        }
        return $answer;
    }
}
