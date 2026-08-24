<?php
// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

class Solution {
    function continuousSubarrays($nums) {
        $ans = 0;
        $left = 0;
        $minQ = [];
        $maxQ = [];
        $n = count($nums);
        for ($right = 0; $right < $n; $right++) {
            while ($minQ && $nums[$minQ[count($minQ) - 1]] > $nums[$right]) array_pop($minQ);
            while ($maxQ && $nums[$maxQ[count($maxQ) - 1]] < $nums[$right]) array_pop($maxQ);
            $minQ[] = $right;
            $maxQ[] = $right;
            while ($nums[$maxQ[0]] - $nums[$minQ[0]] > 2) {
                $left++;
                if ($minQ[0] < $left) array_shift($minQ);
                if ($maxQ[0] < $left) array_shift($maxQ);
            }
            $ans += $right - $left + 1;
        }
        return $ans;
    }
}
