<?php
// LeetCode 2815 - Max Pair Sum in an Array
// https://leetcode.com/problems/max-pair-sum-in-an-array/

class Solution {
    function maxSum($nums) {
        $best = [];
        $ans = -1;
        foreach ($nums as $v) {
            $x = $v;
            $md = 0;
            while ($x > 0) { $md = max($md, $x % 10); $x = intdiv($x, 10); }
            if (isset($best[$md])) {
                $ans = max($ans, $best[$md] + $v);
                $best[$md] = max($best[$md], $v);
            } else $best[$md] = $v;
        }
        return $ans;
    }
}
