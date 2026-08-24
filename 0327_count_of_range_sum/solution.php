<?php
// LeetCode 0327 - Count of Range Sum
// https://leetcode.com/problems/count-of-range-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function countRangeSum($nums, $lower, $upper) {
        $prefix = [0];
        foreach ($nums as $num) {
            $prefix[] = $prefix[count($prefix) - 1] + $num;
        }
        $temp = array_fill(0, count($prefix), 0);
        return $this->mergeSort($prefix, $temp, 0, count($prefix) - 1, $lower, $upper);
    }

    private function mergeSort(&$prefix, &$temp, $left, $right, $lower, $upper) {
        if ($left >= $right) {
            return 0;
        }
        $mid = intdiv($left + $right, 2);
        $count = $this->mergeSort($prefix, $temp, $left, $mid, $lower, $upper);
        $count += $this->mergeSort($prefix, $temp, $mid + 1, $right, $lower, $upper);

        $start = $mid + 1;
        $end = $mid + 1;
        for ($index = $left; $index <= $mid; $index++) {
            while ($start <= $right && $prefix[$start] - $prefix[$index] < $lower) {
                $start++;
            }
            while ($end <= $right && $prefix[$end] - $prefix[$index] <= $upper) {
                $end++;
            }
            $count += $end - $start;
        }

        $tempLeft = $left;
        $tempRight = $mid + 1;
        $write = $left;
        while ($tempLeft <= $mid && $tempRight <= $right) {
            if ($prefix[$tempLeft] <= $prefix[$tempRight]) {
                $temp[$write] = $prefix[$tempLeft];
                $tempLeft++;
            } else {
                $temp[$write] = $prefix[$tempRight];
                $tempRight++;
            }
            $write++;
        }
        while ($tempLeft <= $mid) {
            $temp[$write] = $prefix[$tempLeft];
            $tempLeft++;
            $write++;
        }
        while ($tempRight <= $right) {
            $temp[$write] = $prefix[$tempRight];
            $tempRight++;
            $write++;
        }
        for ($index = $left; $index <= $right; $index++) {
            $prefix[$index] = $temp[$index];
        }
        return $count;
    }
}
