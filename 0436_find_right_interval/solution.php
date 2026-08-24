<?php
// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

class Solution {
    /**
     * @param int[][] $intervals
     * @return int[]
     */
    function findRightInterval($intervals) {
        return $this->find_right_interval($intervals);
    }

    /**
     * @param int[][] $intervals
     * @return int[]
     */
    function find_right_interval($intervals) {
        $indexed = [];
        foreach ($intervals as $index => [$start, $_]) {
            $indexed[] = [$start, $index];
        }
        usort($indexed, fn($left, $right) => $left[0] <=> $right[0]);
        $starts = array_column($indexed, 0);
        $result = [];
        foreach ($intervals as [$start, $end]) {
            $position = $this->lowerBound($starts, $end);
            $result[] = $position === count($starts) ? -1 : $indexed[$position][1];
        }
        return $result;
    }

    /**
     * @param int[] $values
     * @param int $target
     * @return int
     */
    private function lowerBound($values, $target) {
        $left = 0;
        $right = count($values);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($values[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }
}
