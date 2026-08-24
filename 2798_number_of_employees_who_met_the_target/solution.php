<?php
// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution {
    function numberOfEmployeesWhoMetTarget($hours, $target) {
        $ans = 0;
        foreach ($hours as $h) if ($h >= $target) $ans++;
        return $ans;
    }
}
