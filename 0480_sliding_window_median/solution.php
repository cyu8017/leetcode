<?php
// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

class Solution {
    /**
     * @param int[] $nums
     * @param int $k
     * @return float[]
     */
    function medianSlidingWindow($nums, $k) {
        return $this->median_sliding_window($nums, $k);
    }

    /**
     * @param int[] $nums
     * @param int $k
     * @return float[]
     */
    function median_sliding_window($nums, $k) {
        $window = array_values($nums);
        $window = array_slice($window, 0, $k);
        sort($window);
        $result = [];

        $appendMedian = function () use (&$result, &$window, $k) {
            if ($k % 2 === 1) {
                $result[] = (float)$window[intdiv($k, 2)];
            } else {
                $result[] = ($window[$k / 2 - 1] + $window[$k / 2]) / 2.0;
            }
        };

        $appendMedian();
        for ($index = $k; $index < count($nums); $index++) {
            $outgoing = $nums[$index - $k];
            $incoming = $nums[$index];
            $position = $this->bisectLeft($window, $outgoing);
            array_splice($window, $position, 1);
            $insertAt = $this->bisectLeft($window, $incoming);
            array_splice($window, $insertAt, 0, [$incoming]);
            $appendMedian();
        }
        return $result;
    }

    /**
     * @param int[] $array
     * @param int $target
     * @return int
     */
    private function bisectLeft($array, $target) {
        $left = 0;
        $right = count($array);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($array[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }
}
