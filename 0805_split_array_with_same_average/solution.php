<?php
// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function splitArraySameAverage($nums) {
        $n = count($nums);
        $total = 0;
        foreach ($nums as $x) $total += $x;
        sort($nums);
        $memo = [];
        $find = function($target, $count, $index) use (&$find, &$memo, $nums, $n) {
            if ($count === 0) return $target === 0;
            if ($index === $n || $count + $index > $n || $target < 0) return false;
            $key = ($target * 1048576) + ($count * 1024) + $index;
            if (isset($memo[$key])) return false;
            if ($find($target - $nums[$index], $count - 1, $index + 1) || $find($target, $count, $index + 1)) {
                return true;
            }
            $memo[$key] = true;
            return false;
        };
        for ($size = 1; $size < $n; $size++) {
            if (($total * $size) % $n === 0 && $find(intdiv($total * $size, $n), $size, 0)) return true;
        }
        return false;
    }
}
