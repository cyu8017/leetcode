<?php
// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

class Solution {
    function maxSum($grid, $limits, $k) {
        $h = [];
        $sum = 0;
        $push = function($v) use (&$h) {
            $h[] = $v;
            sort($h);
        };
        $poll = function() use (&$h) { return array_shift($h); };
        for ($i = 0; $i < count($grid); $i++) {
            $r = $grid[$i];
            sort($r);
            $lim = $limits[$i];
            if ($lim > count($r)) $lim = count($r);
            for ($j = 0; $j < $lim; $j++) {
                $val = $r[count($r) - 1 - $j];
                $push($val);
                $sum += $val;
                if (count($h) > $k) $sum -= $poll();
            }
        }
        return $sum;
    }
}
