<?php
// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function targetIndices($nums, $target) {
        $less = 0;
        $eq = 0;
        foreach ($nums as $x) {
            if ($x < $target) $less++;
            else if ($x === $target) $eq++;
        }
        $ans = [];
        for ($i = 0; $i < $eq; $i++) $ans[] = $less + $i;
        return $ans;
    }
}
