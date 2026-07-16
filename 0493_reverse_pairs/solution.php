<?php
// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function reversePairs($nums) {
        return $this->reverse_pairs($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function reverse_pairs(&$nums) {
        $mergeSort = function ($start, $end) use (&$mergeSort, &$nums) {
            if ($start >= $end) {
                return 0;
            }
            $mid = intdiv($start + $end, 2);
            $count = $mergeSort($start, $mid) + $mergeSort($mid + 1, $end);
            $j = $mid + 1;
            for ($i = $start; $i <= $mid; $i++) {
                while ($j <= $end && $nums[$i] > 2 * $nums[$j]) {
                    $j++;
                }
                $count += $j - ($mid + 1);
            }
            $slice = array_slice($nums, $start, $end - $start + 1);
            sort($slice);
            array_splice($nums, $start, $end - $start + 1, $slice);
            return $count;
        };

        return $mergeSort(0, count($nums) - 1);
    }
}
