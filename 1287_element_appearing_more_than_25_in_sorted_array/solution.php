<?php
// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findSpecialInteger($arr) {
        $n = count($arr);
        foreach ([intdiv($n, 4), intdiv($n, 2), intdiv(3 * $n, 4)] as $idx) {
            $value = $arr[$idx];
            $count = 0;
            foreach ($arr as $x) if ($x === $value) $count++;
            if ($count > intdiv($n, 4)) return $value;
        }
        return $arr[0];
    }
}
