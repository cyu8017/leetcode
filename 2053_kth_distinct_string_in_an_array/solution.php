<?php
// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution {
    /**
     * @param String[] $arr
     * @param Integer $k
     * @return String
     */
    function kthDistinct($arr, $k) {
        $freq = [];
        foreach ($arr as $s) $freq[$s] = ($freq[$s] ?? 0) + 1;
        foreach ($arr as $s) if ($freq[$s] === 1 && --$k === 0) return $s;
        return "";
    }
}
