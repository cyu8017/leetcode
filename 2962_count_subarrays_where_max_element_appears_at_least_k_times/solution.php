<?php
// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution {
    function countSubarrays($nums, $k) {
        $mx = $nums[0];
        foreach ($nums as $v) if ($v > $mx) $mx = $v;
        $ans = 0;
        $cnt = 0;
        $left = 0;
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            if ($nums[$right] === $mx) $cnt++;
            while ($cnt >= $k) {
                if ($nums[$left] === $mx) $cnt--;
                $left++;
            }
            $ans += $left;
        }
        return $ans;
    }
}
