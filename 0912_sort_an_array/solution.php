<?php
// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

class Solution {
    function sortArray($nums) {
        $n = count($nums);
        if ($n <= 1) return $nums;
        $mid = $n >> 1;
        $left = $this->sortArray(array_slice($nums, 0, $mid));
        $right = $this->sortArray(array_slice($nums, $mid));
        $merged = array_fill(0, $n, 0);
        $i = 0;
        $j = 0;
        $k = 0;
        $ln = count($left);
        $rn = count($right);
        while ($i < $ln && $j < $rn) {
            if ($left[$i] <= $right[$j]) $merged[$k++] = $left[$i++];
            else $merged[$k++] = $right[$j++];
        }
        while ($i < $ln) $merged[$k++] = $left[$i++];
        while ($j < $rn) $merged[$k++] = $right[$j++];
        return $merged;
    }
}
