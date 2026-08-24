<?php
// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

class Solution {
    function taskSchedulerII($tasks, $space) {
        $next = [];
        $day = 0;
        foreach ($tasks as $t) {
            $day = max($day, $next[$t] ?? 0);
            $day++;
            $next[$t] = $day + $space;
        }
        return $day;
    }
}
