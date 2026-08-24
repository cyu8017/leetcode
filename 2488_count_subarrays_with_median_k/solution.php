<?php
// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

class Solution {
    function countSubarrays($nums, $k) {
        $pos = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] === $k) { $pos = $i; break; }
        }
        $bal = [];
        $bal[0] = 1;
        $cur = 0;
        for ($i = $pos - 1; $i >= 0; $i--) {
            $cur += $nums[$i] < $k ? -1 : 1;
            if (!isset($bal[$cur])) $bal[$cur] = 0;
            $bal[$cur]++;
        }
        $ans = (isset($bal[0]) ? $bal[0] : 0) + (isset($bal[1]) ? $bal[1] : 0);
        $cur = 0;
        for ($i = $pos + 1; $i < $n; $i++) {
            $cur += $nums[$i] < $k ? -1 : 1;
            $ans += (isset($bal[-$cur]) ? $bal[-$cur] : 0) + (isset($bal[1 - $cur]) ? $bal[1 - $cur] : 0);
        }
        return $ans;
    }
}
