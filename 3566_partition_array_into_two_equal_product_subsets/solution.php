<?php
// LeetCode 3566 - Partition Array into Two Equal Product Subsets
// https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

class Solution {
    function checkEqualPartitions($nums, $target) {
        $n = count($nums);
        for ($i = 0; $i < (1 << $n); $i++) {
            $x = 1;
            $y = 1;
            for ($j = 0; $j < $n; $j++) {
                if ((($i >> $j) & 1) !== 0) $x *= $nums[$j];
                else $y *= $nums[$j];
                if ($x > $target || $y > $target) break;
            }
            if ($x === $target && $y === $target) return true;
        }
        return false;
    }
}
