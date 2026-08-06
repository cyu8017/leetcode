<?php
// LeetCode 1502 - Can Make Arithmetic Progression From Sequence
// https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canMakeArithmeticProgression($arr) {
        sort($arr);
        $diff = $arr[1] - $arr[0];
        $n = count($arr);
        for ($i = 2; $i < $n; $i++) {
            if ($arr[$i] - $arr[$i - 1] !== $diff) {
                return false;
            }
        }
        return true;
    }
}
