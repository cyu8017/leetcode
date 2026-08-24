<?php
// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

class Solution {
    function filter($arr, $fn) {
        $out = [];
        for ($i = 0; $i < count($arr); $i++) {
            if ($fn($arr[$i], $i)) $out[] = $arr[$i];
        }
        return $out;
    }
}
