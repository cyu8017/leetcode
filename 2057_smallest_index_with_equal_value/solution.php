<?php
// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function smallestEqual($nums) {
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            if ($i % 10 === $nums[$i]) return $i;
        return -1;
    }
}
