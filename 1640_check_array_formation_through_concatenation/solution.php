<?php
// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer[][] $pieces
     * @return Boolean
     */
    function canFormArray($arr, $pieces) {
        $byFirst = [];
        foreach ($pieces as $p) {
            $byFirst[$p[0]] = $p;
        }
        $i = 0;
        $n = count($arr);
        while ($i < $n) {
            if (!isset($byFirst[$arr[$i]])) {
                return false;
            }
            $p = $byFirst[$arr[$i]];
            $plen = count($p);
            for ($j = 0; $j < $plen; $j++) {
                if ($i + $j >= $n || $arr[$i + $j] !== $p[$j]) {
                    return false;
                }
            }
            $i += $plen;
        }
        return true;
    }
}
