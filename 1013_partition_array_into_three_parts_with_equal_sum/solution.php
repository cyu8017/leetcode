<?php
// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution {
    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canThreePartsEqualSum($arr) {
        $total = array_sum($arr);
        if ($total % 3 !== 0) {
            return false;
        }
        $target = intdiv($total, 3);
        $parts = $cur = 0;
        foreach ($arr as $x) {
            $cur += $x;
            if ($cur === $target) {
                $parts++;
                $cur = 0;
            }
        }
        return $parts >= 3;
    }
}
