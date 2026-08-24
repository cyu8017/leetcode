<?php
// LeetCode 0046 - Permutations
// https://leetcode.com/problems/permutations/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function permute($nums) {
        $result = [];
        $path = [];
        $used = array_fill(0, count($nums), false);

        $backtrack = function () use (&$nums, &$result, &$path, &$used, &$backtrack) {
            if (count($path) === count($nums)) {
                $result[] = $path;
                return;
            }

            for ($i = 0; $i < count($nums); $i++) {
                if ($used[$i]) {
                    continue;
                }
                $used[$i] = true;
                $path[] = $nums[$i];
                $backtrack();
                array_pop($path);
                $used[$i] = false;
            }
        };

        $backtrack();
        return $result;
    }
}
