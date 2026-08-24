<?php
// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

class Solution {
    function numberOfGoodPartitions($nums) {
        $mod = 1000000007;
        $last = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) $last[$nums[$i]] = $i;
        $ans = 1;
        $end = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($last[$nums[$i]] > $end) $end = $last[$nums[$i]];
            if ($i === $end && $i !== $n - 1) $ans = (int)(($ans * 2) % $mod);
        }
        return $ans;
    }
}
