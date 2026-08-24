<?php
// LeetCode 0056 - Merge Intervals
// https://leetcode.com/problems/merge-intervals/

class Solution {
    /**
     * @param Integer[][] $intervals
     * @return Integer[][]
     */
    function merge($intervals) {
        usort($intervals, function ($left, $right) {
            return $left[0] <=> $right[0];
        });

        $merged = [$intervals[0]];

        for ($i = 1; $i < count($intervals); $i++) {
            $current = $intervals[$i];
            $lastIndex = count($merged) - 1;

            if ($current[0] <= $merged[$lastIndex][1]) {
                $merged[$lastIndex][1] = max($merged[$lastIndex][1], $current[1]);
            } else {
                $merged[] = $current;
            }
        }

        return $merged;
    }
}
