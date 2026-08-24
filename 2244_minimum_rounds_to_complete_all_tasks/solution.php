<?php
// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution {
    function minimumRounds($tasks) {
        $freq = [];
        foreach ($tasks as $t) $freq[$t] = ($freq[$t] ?? 0) + 1;
        $ans = 0;
        foreach ($freq as $c) {
            if ($c === 1) return -1;
            $ans += intdiv($c + 2, 3);
        }
        return $ans;
    }
}
