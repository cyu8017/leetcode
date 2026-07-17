<?php
// LeetCode 1822 - Sign of the Product of an Array
// https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function arraySign($nums) {
        $sign = 1;
        foreach ($nums as $num) {
            if ($num === 0) {
                return 0;
            }
            if ($num < 0) {
                $sign = -$sign;
            }
        }
        return $sign;
    }
}
