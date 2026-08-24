<?php
// LeetCode 3737 - Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/

class Solution {
    function countMajoritySubarrays($nums, $target) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cnt = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($nums[$j] === $target) $cnt++;
                if ($cnt * 2 > $j - $i + 1) $ans++;
            }
        }
        return $ans;
    }
}
