<?php
// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

class Solution {
    function chunk($arr, $size) {
        $ans = [];
        for ($i = 0; $i < count($arr); $i += $size) {
            $ans[] = array_slice($arr, $i, $size);
        }
        return $ans;
    }
}
