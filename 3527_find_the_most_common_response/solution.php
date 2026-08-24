<?php
// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

class Solution {
    function findCommonResponse($responses) {
        $cnt = [];
        foreach ($responses as $ws) {
            $s = [];
            foreach ($ws as $w) {
                if (!isset($s[$w])) {
                    $s[$w] = true;
                    $cnt[$w] = ($cnt[$w] ?? 0) + 1;
                }
            }
        }
        $ans = $responses[0][0];
        foreach ($cnt as $w => $v) {
            if ($cnt[$ans] < $v || ($cnt[$ans] === $v && $w < $ans)) $ans = $w;
        }
        return $ans;
    }
}
