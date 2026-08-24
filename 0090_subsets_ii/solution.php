<?php
// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function subsetsWithDup($nums) {
        sort($nums);
        $result = [];
        $path = [];

        $backtrack = function ($start) use (&$nums, &$result, &$path, &$backtrack) {
            $result[] = $path;
            for ($i = $start; $i < count($nums); $i++) {
                if ($i > $start && $nums[$i] === $nums[$i - 1]) {
                    continue;
                }
                $path[] = $nums[$i];
                $backtrack($i + 1);
                array_pop($path);
            }
        };

        $backtrack(0);
        return $result;
    }
}
