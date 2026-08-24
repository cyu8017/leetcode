<?php
// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

class Solution {
    function countPartitions($nums) {
        $total = 0;
        foreach ($nums as $x) $total += $x;
        $ans = 0;
        $left = 0;
        for ($i = 0; $i < count($nums) - 1; $i++) {
            $left += $nums[$i];
            if (($left - ($total - $left)) % 2 === 0) $ans++;
        }
        return $ans;
    }
}
