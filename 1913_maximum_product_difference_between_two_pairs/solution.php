<?php
// LeetCode 1913 - Maximum Product Difference Between Two Pairs
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProductDifference($nums) {
        $a = $b = 0;
        $c = $d = 100000;
        foreach ($nums as $x) {
            if ($x > $a) {
                $b = $a;
                $a = $x;
            } elseif ($x > $b) {
                $b = $x;
            }
            if ($x < $c) {
                $d = $c;
                $c = $x;
            } elseif ($x < $d) {
                $d = $x;
            }
        }
        return $a * $b - $c * $d;
    }
}
