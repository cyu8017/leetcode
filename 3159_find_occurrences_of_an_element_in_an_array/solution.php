<?php
// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

class Solution {
    function occurrencesOfElement($nums, $queries, $x) {
        $ids = [];
        for ($i = 0; $i < count($nums); $i++) if ($nums[$i] === $x) $ids[] = $i;
        $ans = [];
        for ($qi = 0; $qi < count($queries); $qi++) {
            $i = $queries[$qi];
            if ($i - 1 < count($ids)) $ans[$qi] = $ids[$i - 1];
            else $ans[$qi] = -1;
        }
        return $ans;
    }
}
