<?php
// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

class Solution {
    function maximumWidth($planks) {
        $cnt = [];
        foreach ($planks as $x) $cnt[$x] = ($cnt[$x] ?? 0) + 1;
        $t = [];
        $ans = 0;
        foreach ($cnt as $x => $v1) {
            $t[$x] = ($t[$x] ?? 0) + $v1;
            $ans = max($ans, $t[$x]);
            $t[$x * 2] = ($t[$x * 2] ?? 0) + intdiv($v1, 2);
            $ans = max($ans, $t[$x * 2]);
            foreach ($cnt as $y => $v2) {
                if ($y > $x) {
                    $key = $x + $y;
                    $t[$key] = ($t[$key] ?? 0) + min($v1, $v2);
                    $ans = max($ans, $t[$key]);
                }
            }
        }
        return $ans;
    }
}
