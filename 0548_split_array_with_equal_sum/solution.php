<?php
// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function splitArray($nums) {
        $n = count($nums);
        if ($n < 7) {
            return false;
        }

        $prefix = [0];
        foreach ($nums as $value) {
            $prefix[] = $prefix[count($prefix) - 1] + $value;
        }

        for ($j = 3; $j < $n - 3; $j++) {
            $seen = [];
            for ($i = 1; $i < $j - 1; $i++) {
                $first = $prefix[$i] - $prefix[0];
                $second = $prefix[$j] - $prefix[$i + 1];
                if ($first === $second) {
                    $seen[$first] = true;
                }
            }

            for ($k = $j + 2; $k < $n - 1; $k++) {
                $third = $prefix[$k] - $prefix[$j + 1];
                $fourth = $prefix[$n] - $prefix[$k + 1];
                if ($third === $fourth && isset($seen[$third])) {
                    return true;
                }
            }
        }

        return false;
    }
}
