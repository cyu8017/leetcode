<?php
// LeetCode 4012 - Count of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

class Solution {
    function countTasks($tasks, $shifts) {
        $m = count($tasks);
        $n = count($shifts);
        $s = array_fill(0, $m + 1, 0);
        for ($i = 0; $i < $m; $i++) $s[$i + 1] = $s[$i] + $tasks[$i];
        $ans = array_fill(0, $n, 0);
        $iIdx = 0;
        $cur = 0;
        for ($j = 0; $j < $n; $j++) {
            if ($shifts[$j] < $tasks[$iIdx] - $cur) {
                $cur += $shifts[$j];
                $ans[$j] = $m - $iIdx;
            } else {
                $t = $shifts[$j] - ($tasks[$iIdx] - $cur);
                if ($t >= $s[$m] - $s[$iIdx + 1]) {
                    $iIdx = 0;
                    $cur = 0;
                } else {
                    $l = $iIdx + 1;
                    $r = $m;
                    while ($l < $r) {
                        $mid = ($l + $r) >> 1;
                        if ($t < $s[$mid + 1] - $s[$iIdx + 1]) $r = $mid;
                        else $l = $mid + 1;
                    }
                    $cur = $t - ($s[$l] - $s[$iIdx + 1]);
                    $iIdx = $l;
                    $ans[$j] = $m - $iIdx;
                }
            }
        }
        return $ans;
    }
}
