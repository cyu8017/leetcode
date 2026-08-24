<?php
// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

class Solution {
    function findClosestNumber($nums) {
        $ans = $nums[0];
        foreach ($nums as $x) {
            if (abs($x) < abs($ans) || (abs($x) === abs($ans) && $x > $ans)) $ans = $x;
        }
        return $ans;
    }
}
