<?php
// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

class Solution {
    function countDays($days, $meetings) {
        usort($meetings, function ($a, $b) { return $a[0] <=> $b[0]; });
        $last = 0;
        $ans = 0;
        foreach ($meetings as $e) {
            $st = $e[0];
            $ed = $e[1];
            if ($last < $st) $ans += $st - $last - 1;
            $last = max($last, $ed);
        }
        $ans += $days - $last;
        return $ans;
    }
}
