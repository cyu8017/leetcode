<?php
// LeetCode 3727 - Maximum Alternating Sum of Squares
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution {
    function maxAlternatingSum($nums) {
        $a = [];
        foreach ($nums as $x) $a[] = $x * $x;
        sort($a);
        $m = intdiv(count($a), 2);
        $ans = 0;
        for ($i = 0; $i < $m; $i++) $ans -= $a[$i];
        for ($i = $m; $i < count($a); $i++) $ans += $a[$i];
        return $ans;
    }
}
