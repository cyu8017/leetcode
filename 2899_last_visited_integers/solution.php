<?php
// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

class Solution {
    function lastVisitedIntegers($nums) {
        $seen = [];
        $ans = [];
        $k = 0;
        foreach ($nums as $v) {
            if ($v !== -1) {
                $seen[] = $v;
                $k = 0;
            } else {
                $k++;
                if ($k > count($seen)) $ans[] = -1;
                else $ans[] = $seen[count($seen) - $k];
            }
        }
        return $ans;
    }
}
