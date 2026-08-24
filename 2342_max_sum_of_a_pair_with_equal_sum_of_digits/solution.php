<?php
// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

class Solution {
    function maximumSum($nums) {
        $best = [];
        $ans = -1;
        foreach ($nums as $x) {
            $ds = $this->digitSum($x);
            if (isset($best[$ds])) {
                $ans = max($ans, $best[$ds] + $x);
                if ($x > $best[$ds]) $best[$ds] = $x;
            } else {
                $best[$ds] = $x;
            }
        }
        return $ans;
    }

    private function digitSum($x) {
        $s = 0;
        while ($x > 0) { $s += $x % 10; $x = intdiv($x, 10); }
        return $s;
    }
}
