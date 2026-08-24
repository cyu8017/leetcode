<?php
// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function reorderedPowerOf2($n) {
        $sig = function($x) {
            $chars = str_split((string)$x);
            sort($chars);
            return implode('', $chars);
        };
        $target = $sig($n);
        for ($i = 0; $i < 31; $i++) if ($sig(1 << $i) === $target) return true;
        return false;
    }
}
