<?php
// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

class Solution {
    function maxFrequencyElements($nums) {
        $cnt = array_fill(0, 101, 0);
        foreach ($nums as $x) $cnt[$x]++;
        $mx = -1;
        $ans = 0;
        foreach ($cnt as $x) {
            if ($mx < $x) {
                $mx = $x;
                $ans = $x;
            } else if ($mx === $x) {
                $ans += $x;
            }
        }
        return $ans;
    }
}
