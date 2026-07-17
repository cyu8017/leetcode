<?php
// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

class Solution {
    /**
     * @param Integer[][] $groups
     * @param Integer[] $nums
     * @return Boolean
     */
    function canChoose($groups, $nums) {
        return $this->dfs($groups, $nums, 0, 0);
    }

    private function dfs($groups, $nums, $i, $start) {
        $n = count($nums);
        if ($i === count($groups)) {
            return $start === $n;
        }
        $g = $groups[$i];
        $m = count($g);
        for ($j = $start; $j <= $n - $m; $j++) {
            if (array_slice($nums, $j, $m) === $g && $this->dfs($groups, $nums, $i + 1, $j + $m)) {
                return true;
            }
        }
        return false;
    }
}
