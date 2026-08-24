<?php
// LeetCode 2834 - Find the Minimum Possible Sum of a Beautiful Array
// https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

class Solution {
    function minimumPossibleSum($n, $target) {
        $MOD = 1000000007;
        $m = intdiv($target, 2);
        if ($n <= $m) return (int)(($n * ($n + 1) / 2) % $MOD);
        $sum = $m * ($m + 1) / 2;
        $remain = $n - $m;
        $sum += $remain * $target + $remain * ($remain - 1) / 2;
        return (int)($sum % $MOD);
    }
}
