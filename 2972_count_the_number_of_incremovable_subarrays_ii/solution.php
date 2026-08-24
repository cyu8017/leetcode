<?php
// LeetCode 2972 - Count the Number of Incremovable Subarrays II
// https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

class Solution {
    function incremovableSubarrayCount($nums) {
        $n = count($nums);
        $left = 0;
        while ($left + 1 < $n && $nums[$left] < $nums[$left + 1]) $left++;
        if ($left === $n - 1) return intdiv($n * ($n + 1), 2);
        $ans = $left + 2;
        $right = $n - 1;
        while ($right > 0 && ($right === $n - 1 || $nums[$right] < $nums[$right + 1])) {
            while ($left >= 0 && $nums[$left] >= $nums[$right]) $left--;
            $ans += $left + 2;
            $right--;
            if ($right > 0 && $nums[$right] >= $nums[$right + 1]) break;
        }
        return $ans;
    }
}
