<?php
// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function uniqueOccurrences($arr) {
        $counts = array_count_values($arr);
        return count($counts) === count(array_unique($counts));
    }
}
