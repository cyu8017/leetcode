<?php
// LeetCode 0658 - Find K Closest Elements
// https://leetcode.com/problems/find-k-closest-elements/

class Solution {
    function findClosestElements($arr, $k, $x) {
        $left = 0;
        $right = count($arr) - $k;
        while ($left < $right) {
            $mid = $left + intdiv($right - $left, 2);
            if ($x - $arr[$mid] > $arr[$mid + $k] - $x) $left = $mid + 1;
            else $right = $mid;
        }
        return array_slice($arr, $left, $k);
    }
}
