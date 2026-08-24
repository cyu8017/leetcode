<?php
// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution {
    function uniformArray($nums1) {
        $mn = PHP_INT_MAX;
        foreach ($nums1 as $x) {
            if ($x % 2 === 1 && $x < $mn) $mn = $x;
        }
        foreach ($nums1 as $x) {
            if ($x % 2 === 0 && $mn !== PHP_INT_MAX && $x < $mn) return false;
        }
        return true;
    }
}
