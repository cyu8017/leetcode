<?php
// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

class Solution {
    function numberOfSubarrays($nums) {
        $stk = [];
        $ans = 0;
        foreach ($nums as $x) {
            while ($stk && $stk[count($stk) - 1][0] < $x) array_pop($stk);
            if (!$stk || $stk[count($stk) - 1][0] > $x) $stk[] = [$x, 1];
            else $stk[count($stk) - 1][1]++;
            $ans += $stk[count($stk) - 1][1];
        }
        return $ans;
    }
}
