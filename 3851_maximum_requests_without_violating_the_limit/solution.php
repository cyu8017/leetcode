<?php
// LeetCode 3851 - Maximum Requests Without Violating the Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

class Solution {
    function maxRequests($requests, $k, $window) {
        $g = [];
        foreach ($requests as $r) {
            $g[$r[0]][] = $r[1];
        }
        $ans = count($requests);
        foreach ($g as $ts) {
            sort($ts);
            $kept = [];
            foreach ($ts as $t) {
                while (count($kept) > 0 && $t - $kept[0] > $window) array_shift($kept);
                if (count($kept) < $k) $kept[] = $t;
                else $ans--;
            }
        }
        return $ans;
    }
}
