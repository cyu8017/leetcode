<?php
// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

class Solution {
    function minProcessingTime($processorTime, $tasks) {
        sort($processorTime);
        rsort($tasks);
        $ans = 0;
        $p = count($processorTime);
        for ($i = 0; $i < $p; $i++) {
            $fin = $processorTime[$i] + $tasks[$i * 4];
            if ($fin > $ans) $ans = $fin;
        }
        return $ans;
    }
}
