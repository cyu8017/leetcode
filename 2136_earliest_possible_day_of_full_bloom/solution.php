<?php
// LeetCode 2136 - Earliest Possible Day of Full Bloom
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution {
    /**
     * @param Integer[] $plantTime
     * @param Integer[] $growTime
     * @return Integer
     */
    function earliestFullBloom($plantTime, $growTime) {
        $n = count($plantTime);
        $idx = range(0, $n - 1);
        usort($idx, function($a, $b) use ($growTime) { return $growTime[$b] - $growTime[$a]; });
        $day = 0;
        $ans = 0;
        foreach ($idx as $i) {
            $day += $plantTime[$i];
            $ans = max($ans, $day + $growTime[$i]);
        }
        return $ans;
    }
}
