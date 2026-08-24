<?php
// LeetCode 3871 - Count Commas in Range II
// https://leetcode.com/problems/count-commas-in-range-ii/

class Solution {
    function countCommas($n) {
        $ans = 0;
        for ($x = 1000; $x <= $n; $x *= 1000) $ans += $n - $x + 1;
        return $ans;
    }
}
