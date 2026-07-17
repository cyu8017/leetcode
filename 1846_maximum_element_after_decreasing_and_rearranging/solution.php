<?php
// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maximumElementAfterDecrementingAndRearranging($arr) {
        sort($arr);
        $arr[0] = 1;
        for ($i = 1; $i < count($arr); $i++) {
            $arr[$i] = min($arr[$i], $arr[$i - 1] + 1);
        }
        return max($arr);
    }
}
