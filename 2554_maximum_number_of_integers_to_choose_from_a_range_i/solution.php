<?php
// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution {
    function maxCount($banned, $n, $maxSum) {
        $ban = [];
        foreach ($banned as $x) $ban[$x] = true;
        $ans = 0;
        $sum = 0;
        for ($i = 1; $i <= $n; $i++) {
            if (isset($ban[$i])) continue;
            if ($sum + $i > $maxSum) break;
            $sum += $i;
            $ans++;
        }
        return $ans;
    }
}
