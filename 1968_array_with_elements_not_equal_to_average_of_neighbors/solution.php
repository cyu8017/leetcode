<?php
// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function rearrangeArray($nums) {
        sort($nums);
        $n = count($nums);
        $mid = intdiv($n + 1, 2);
        $small = array_slice($nums, 0, $mid);
        $large = array_slice($nums, $mid);
        $ans = [];
        $i = 0;
        $j = 0;
        while ($i < count($small) || $j < count($large)) {
            if ($i < count($small)) {
                $ans[] = $small[$i++];
            }
            if ($j < count($large)) {
                $ans[] = $large[$j++];
            }
        }
        return $ans;
    }
}
