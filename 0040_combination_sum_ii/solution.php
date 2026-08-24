<?php
// LeetCode 0040 - Combination Sum II
// https://leetcode.com/problems/combination-sum-ii/

class Solution {
    /**
     * @param Integer[] $candidates
     * @param Integer $target
     * @return Integer[][]
     */
    function combinationSum2($candidates, $target) {
        sort($candidates);
        $result = [];
        $path = [];

        $backtrack = function ($start, $remaining) use (&$candidates, &$result, &$path, &$backtrack) {
            if ($remaining === 0) {
                $result[] = $path;
                return;
            }
            if ($remaining < 0) {
                return;
            }

            for ($i = $start; $i < count($candidates); $i++) {
                if ($i > $start && $candidates[$i] === $candidates[$i - 1]) {
                    continue;
                }
                $path[] = $candidates[$i];
                $backtrack($i + 1, $remaining - $candidates[$i]);
                array_pop($path);
            }
        };

        $backtrack(0, $target);
        return $result;
    }
}
