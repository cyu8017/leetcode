<?php
// LeetCode 2656 - Maximum Sum With Exactly K Elements
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution {
    function maximizeSum($nums, $k) {
        $mx = $nums[0];
        foreach ($nums as $x) if ($x > $mx) $mx = $x;
        return $k * $mx + intdiv($k * ($k - 1), 2);
    }
}
