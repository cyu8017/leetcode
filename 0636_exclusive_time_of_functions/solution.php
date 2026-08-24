<?php
// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

class Solution {
    function exclusiveTime($n, $logs) {
        $result = array_fill(0, $n, 0);
        $stack = [];
        $prevTime = 0;
        foreach ($logs as $log) {
            $parts = explode(":", $log);
            $funcId = intval($parts[0]);
            $event = $parts[1];
            $time = intval($parts[2]);
            if ($event === "start") {
                if ($stack) $result[$stack[count($stack) - 1]] += $time - $prevTime;
                $stack[] = $funcId;
                $prevTime = $time;
            } else {
                $result[array_pop($stack)] += $time - $prevTime + 1;
                $prevTime = $time + 1;
            }
        }
        return $result;
    }
}
