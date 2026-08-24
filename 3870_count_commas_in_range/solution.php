<?php
// LeetCode 3870 - Count Commas in Range
// https://leetcode.com/problems/count-commas-in-range/

class Solution {
    function countCommas($n) {
        return max(0, $n - 999);
    }
}
