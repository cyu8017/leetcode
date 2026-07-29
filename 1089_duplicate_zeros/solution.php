<?php
// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

class Solution {
    /**
     * @param Integer[] $arr
     * @return NULL
     */
    function duplicateZeros(&$arr) {
        $zeros = 0;
        foreach ($arr as $v) {
            if ($v === 0) {
                $zeros++;
            }
        }
        $n = count($arr);
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($i + $zeros < $n) {
                $arr[$i + $zeros] = $arr[$i];
            }
            if ($arr[$i] === 0) {
                $zeros--;
                if ($i + $zeros < $n) {
                    $arr[$i + $zeros] = 0;
                }
            }
        }
    }
}
