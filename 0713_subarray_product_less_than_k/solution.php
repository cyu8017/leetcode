<?php
// LeetCode 0713 - Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

class Solution {
    function numSubarrayProductLessThanK($nums, $k) {
        if ($k <= 1) return 0;
        $product = 1;
        $left = 0;
        $ans = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            $product *= $nums[$right];
            while ($product >= $k) $product = intdiv($product, $nums[$left++]);
            $ans += $right - $left + 1;
        }
        return $ans;
    }
}
