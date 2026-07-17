<?php
// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

class Solution {
    /**
     * @param Integer[] $target
     * @param Integer[] $arr
     * @return Integer
     */
    function minOperations($target, $arr) {
        $pos = [];
        foreach ($target as $i => $value) {
            $pos[$value] = $i;
        }
        $lis = [];
        foreach ($arr as $value) {
            if (!array_key_exists($value, $pos)) {
                continue;
            }
            $idx = $pos[$value];
            $lo = 0;
            $hi = count($lis);
            while ($lo < $hi) {
                $mid = intdiv($lo + $hi, 2);
                if ($lis[$mid] < $idx) {
                    $lo = $mid + 1;
                } else {
                    $hi = $mid;
                }
            }
            if ($lo === count($lis)) {
                $lis[] = $idx;
            } else {
                $lis[$lo] = $idx;
            }
        }
        return count($target) - count($lis);
    }
}
