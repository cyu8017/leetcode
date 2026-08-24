<?php
// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

class Solution {
    private function check($nums, $target, $kk) {
        $cnt = 0;
        $sign = 1;
        $n = count($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            $x = $nums[$i] * $sign;
            if ($x === $target) $sign = 1;
            else {
                $sign = -1;
                $cnt++;
            }
        }
        return $cnt <= $kk && $nums[$n - 1] * $sign === $target;
    }

    function canMakeEqual($nums, $k) {
        return $this->check($nums, $nums[0], $k) || $this->check($nums, -$nums[0], $k);
    }
}
