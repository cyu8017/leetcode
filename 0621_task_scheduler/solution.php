<?php
// LeetCode 0621 - Task Scheduler
// https://leetcode.com/problems/task-scheduler/

class Solution {
    function leastInterval($tasks, $n) {
        $counts = array_fill(0, 26, 0);
        foreach ($tasks as $task) ++$counts[ord($task) - 65];
        $maxFreq = 0;
        foreach ($counts as $count) $maxFreq = max($maxFreq, $count);
        $maxCount = 0;
        foreach ($counts as $count) if ($count === $maxFreq) ++$maxCount;
        return max(count($tasks), ($maxFreq - 1) * ($n + 1) + $maxCount);
    }
}
