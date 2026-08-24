<?php
// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

class Solution {
    function sortBy($arr, $fn) {
        $out = $arr;
        usort($out, function($a, $b) use ($fn) { return $fn($a) <=> $fn($b); });
        return $out;
    }
}
