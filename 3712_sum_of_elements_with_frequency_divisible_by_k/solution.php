<?php
// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

class Solution {
    function sumDivisibleByK($nums, $k) {
        $cnt = [];
        foreach ($nums as $x) {
            if (!isset($cnt[$x])) $cnt[$x] = 0;
            $cnt[$x]++;
        }
        $ans = 0;
        foreach ($cnt as $key => $val) {
            if ($val % $k === 0) $ans += $key * $val;
        }
        return $ans;
    }
}
