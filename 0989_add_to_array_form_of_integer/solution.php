<?php
// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution {
    /**
     * @param Integer[] $num
     * @param Integer $k
     * @return Integer[]
     */
    function addToArrayForm($num, $k) {
        $list = $num;
        $i = count($list) - 1;
        while ($k > 0 || $i >= 0) {
            if ($i >= 0) {
                $k += $list[$i];
                $list[$i] = $k % 10;
                $i--;
            } else {
                array_unshift($list, $k % 10);
            }
            $k = intdiv($k, 10);
        }
        return $list;
    }
}
