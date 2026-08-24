<?php
// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

class Solution {
    function minArrayLength($nums, $k) {
        if (count($nums) === 0) return 0;
        $ans = 1;
        $prod = $nums[0];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            if ($prod <= $k && $nums[$i] <= $k && ($nums[$i] === 0 || $prod <= intdiv($k, $nums[$i]))) {
                $prod *= $nums[$i];
            } else {
                $ans++;
                $prod = $nums[$i];
            }
        }
        return $ans;
    }
}
