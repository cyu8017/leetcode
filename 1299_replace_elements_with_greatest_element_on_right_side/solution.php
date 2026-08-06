<?php
// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function replaceElements($arr) {
        $greatest = -1;
        for ($i = count($arr) - 1; $i >= 0; $i--) {
            $cur = $arr[$i];
            $arr[$i] = $greatest;
            $greatest = max($greatest, $cur);
        }
        return $arr;
    }
}
