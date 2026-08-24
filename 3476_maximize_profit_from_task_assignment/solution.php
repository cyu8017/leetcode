<?php
// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

class Solution {
    function maxProfit($workers, $tasks) {
        sort($workers);
        usort($tasks, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = 0;
        $used = array_fill(0, count($tasks), false);
        foreach ($workers as $w) {
            $best = -1;
            $bi = -1;
            for ($i = 0; $i < count($tasks); $i++) {
                if ($used[$i]) continue;
                if ($tasks[$i][0] > $w) break;
                if ($tasks[$i][1] > $best) {
                    $best = $tasks[$i][1];
                    $bi = $i;
                }
            }
            if ($bi >= 0) {
                $used[$bi] = true;
                $ans += $best;
            }
        }
        return $ans;
    }
}
