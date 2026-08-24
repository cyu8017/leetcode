<?php
// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/

class Solution {
    function triangleNumber($nums) {
        sort($nums);
        $n = count($nums);
        $count = 0;
        for ($k = $n - 1; $k >= 2; --$k) {
            $left = 0;
            $right = $k - 1;
            while ($left < $right) {
                if ($nums[$left] + $nums[$right] > $nums[$k]) {
                    $count += $right - $left;
                    --$right;
                } else {
                    ++$left;
                }
            }
        }
        return $count;
    }
}
