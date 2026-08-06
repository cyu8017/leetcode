<?php
// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer[]
     */
    function relativeSortArray($arr1, $arr2) {
        $order = array_flip($arr2);
        usort($arr1, function ($a, $b) use ($order) {
            $ia = $order[$a] ?? PHP_INT_MAX;
            $ib = $order[$b] ?? PHP_INT_MAX;
            if ($ia !== $ib) return $ia <=> $ib;
            return $a <=> $b;
        });
        return $arr1;
    }
}
