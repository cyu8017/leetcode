<?php
// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

class Solution {
    function map($arr, $fn) {
        $out = [];
        for ($i = 0; $i < count($arr); $i++) $out[$i] = $fn($arr[$i], $i);
        return $out;
    }
}
