<?php
// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

class Solution {
    function earliestTime($tasks) {
        $ans = 200;
        foreach ($tasks as $task) $ans = min($ans, $task[0] + $task[1]);
        return $ans;
    }
}
