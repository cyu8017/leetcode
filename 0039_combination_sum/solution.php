<?php
// LeetCode 0039 - Combination Sum
// https://leetcode.com/problems/combination-sum/

class Solution {
    /**
     * @param Integer[] $candidates
     * @param Integer $target
     * @return Integer[][]
     */
    function combinationSum($candidates, $target) {
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
                $path[] = $candidates[$i];
                $backtrack($i, $remaining - $candidates[$i]);
                array_pop($path);
            }
        };

        $backtrack(0, $target);
        return $result;
    }
}
