<?php
// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

class Solution {
    function maximumSwap($num) {
        $digits = str_split(strval($num));
        $last = array_fill(0, 10, -1);
        for ($i = 0; $i < count($digits); ++$i) $last[ord($digits[$i]) - 48] = $i;
        for ($i = 0; $i < count($digits); ++$i) {
            for ($candidate = 9; $candidate > ord($digits[$i]) - 48; --$candidate) {
                if ($last[$candidate] > $i) {
                    $j = $last[$candidate];
                    $tmp = $digits[$i]; $digits[$i] = $digits[$j]; $digits[$j] = $tmp;
                    return intval(implode("", $digits));
                }
            }
        }
        return $num;
    }
}
