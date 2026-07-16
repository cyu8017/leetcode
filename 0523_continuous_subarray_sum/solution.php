<?php
// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function checkSubarraySum($nums, $k) {
        return $this->check_subarray_sum($nums, $k);
    }

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function check_subarray_sum($nums, $k) {
        $prefix = 0;
        $remainders = [0 => -1];
        foreach ($nums as $index => $num) {
            $prefix += $num;
            $mod = $k === 0 ? $prefix : $prefix % $k;
            if (array_key_exists($mod, $remainders)) {
                if ($index - $remainders[$mod] >= 2) {
                    return true;
                }
            } else {
                $remainders[$mod] = $index;
            }
        }
        return false;
    }
}
