<?php
// LeetCode 2270 - Number of Ways to Split Array
// https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution {
    function waysToSplitArray($nums) {
        $total = 0;
        foreach ($nums as $v) $total += $v;
        $left = 0;
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i + 1 < $n; $i++) {
            $left += $nums[$i];
            if ($left >= $total - $left) $ans++;
        }
        return $ans;
    }
}
