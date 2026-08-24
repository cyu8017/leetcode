<?php
// LeetCode 2871 - Split Array Into Maximum Number of Subarrays
// https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

class Solution {
    function maxSubarrays($nums) {
        $ans = 0;
        $cur = -1;
        foreach ($nums as $v) {
            if ($cur === -1) $cur = $v;
            else $cur &= $v;
            if ($cur === 0) {
                $ans++;
                $cur = -1;
            }
        }
        return $ans === 0 ? 1 : $ans;
    }
}
