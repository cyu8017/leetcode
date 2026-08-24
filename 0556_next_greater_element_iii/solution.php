<?php
// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

class Solution {
    function nextGreaterElement($n) {
        $digits = str_split(strval($n));
        $i = count($digits) - 2;
        while ($i >= 0 && $digits[$i] >= $digits[$i + 1]) --$i;
        if ($i < 0) return -1;
        $j = count($digits) - 1;
        while ($digits[$j] <= $digits[$i]) --$j;
        $tmp = $digits[$i]; $digits[$i] = $digits[$j]; $digits[$j] = $tmp;
        $left = $i + 1;
        $right = count($digits) - 1;
        while ($left < $right) {
            $tmp = $digits[$left]; $digits[$left] = $digits[$right]; $digits[$right] = $tmp;
            ++$left;
            --$right;
        }
        $value = intval(implode("", $digits));
        return $value > 2147483647 ? -1 : $value;
    }
}
