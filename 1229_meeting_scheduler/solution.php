<?php
// LeetCode 1229 - Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler/

class Solution {
    /**
     * @param Integer[][] $slots1
     * @param Integer[][] $slots2
     * @param Integer $duration
     * @return Integer[]
     */
    function minAvailableDuration($slots1, $slots2, $duration) {
        usort($slots1, fn($a, $b) => $a[0] <=> $b[0]);
        usort($slots2, fn($a, $b) => $a[0] <=> $b[0]);
        $i = $j = 0;
        while ($i < count($slots1) && $j < count($slots2)) {
            $start = max($slots1[$i][0], $slots2[$j][0]);
            $end = min($slots1[$i][1], $slots2[$j][1]);
            if ($end - $start >= $duration) return [$start, $start + $duration];
            if ($slots1[$i][1] < $slots2[$j][1]) $i++;
            else $j++;
        }
        return [];
    }
}
