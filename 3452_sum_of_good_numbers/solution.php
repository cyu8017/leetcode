<?php
// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

class Solution {
    function sumOfGoodNumbers($nums, $k) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $x = $nums[$i];
            $good = true;
            if ($i - $k >= 0 && $x <= $nums[$i - $k]) $good = false;
            if ($i + $k < $n && $x <= $nums[$i + $k]) $good = false;
            if ($good) $ans += $x;
        }
        return $ans;
    }
}
