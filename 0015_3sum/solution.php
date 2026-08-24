<?php
// LeetCode 0015 - 3Sum
// https://leetcode.com/problems/3sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function threeSum($nums) {
        sort($nums);
        $result = [];
        $n = count($nums);

        for ($i = 0; $i < $n - 2; $i++) {
            if ($i > 0 && $nums[$i] === $nums[$i - 1]) {
                continue;
            }

            $left = $i + 1;
            $right = $n - 1;
            while ($left < $right) {
                $total = $nums[$i] + $nums[$left] + $nums[$right];
                if ($total === 0) {
                    $result[] = [$nums[$i], $nums[$left], $nums[$right]];
                    while ($left < $right && $nums[$left] === $nums[$left + 1]) {
                        $left++;
                    }
                    while ($left < $right && $nums[$right] === $nums[$right - 1]) {
                        $right--;
                    }
                    $left++;
                    $right--;
                } elseif ($total < 0) {
                    $left++;
                } else {
                    $right--;
                }
            }
        }

        return $result;
    }
}
