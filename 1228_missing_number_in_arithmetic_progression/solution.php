<?php
// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function missingNumber($arr) {
        $n = count($arr);
        $difference = intdiv($arr[$n - 1] - $arr[0], $n);
        for ($i = 1; $i < $n; $i++) {
            $expected = $arr[0] + $i * $difference;
            if ($arr[$i] !== $expected) return $expected;
        }
        return $arr[0];
    }
}
