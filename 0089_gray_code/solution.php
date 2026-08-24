<?php
// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

class Solution {
    /**
     * @param Integer $n
     * @return Integer[]
     */
    function grayCode($n) {
        $size = 1 << $n;
        $result = [];
        for ($i = 0; $i < $size; $i++) {
            $result[] = $i ^ ($i >> 1);
        }
        return $result;
    }
}
