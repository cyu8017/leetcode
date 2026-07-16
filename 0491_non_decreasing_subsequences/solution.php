<?php
// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function findSubsequences($nums) {
        return $this->find_subsequences($nums);
    }

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function find_subsequences($nums) {
        $result = [];

        $backtrack = function ($start, $path) use (&$backtrack, $nums, &$result) {
            if (count($path) >= 2) {
                $result[json_encode($path)] = $path;
            }
            $used = [];
            for ($index = $start; $index < count($nums); $index++) {
                if (isset($used[$nums[$index]])) {
                    continue;
                }
                if ($path !== [] && $nums[$index] < $path[count($path) - 1]) {
                    continue;
                }
                $used[$nums[$index]] = true;
                $path[] = $nums[$index];
                $backtrack($index + 1, $path);
                array_pop($path);
            }
        };

        $backtrack(0, []);
        $values = array_values($result);
        sort($values);
        return $values;
    }
}
