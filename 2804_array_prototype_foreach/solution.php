<?php
// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

class Solution {
    function forEachOnArray($arr, $callback, $context = null) {
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            if (is_callable($callback)) $callback($arr[$i], $i, $arr, $context);
        }
        return $arr;
    }
}
