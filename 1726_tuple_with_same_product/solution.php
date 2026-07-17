<?php
// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function tupleSameProduct($nums) {
        $counts = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $product = $nums[$i] * $nums[$j];
                $counts[$product] = ($counts[$product] ?? 0) + 1;
            }
        }
        $result = 0;
        foreach ($counts as $count) {
            $result += $count * ($count - 1) * 4;
        }
        return $result;
    }
}
