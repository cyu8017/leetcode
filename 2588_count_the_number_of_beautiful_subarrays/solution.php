<?php
// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

class Solution {
    function beautifulSubarrays($nums) {
        $freq = [0 => 1];
        $xorv = 0;
        $ans = 0;
        foreach ($nums as $x) {
            $xorv ^= $x;
            $ans += $freq[$xorv] ?? 0;
            $freq[$xorv] = ($freq[$xorv] ?? 0) + 1;
        }
        return $ans;
    }
}
