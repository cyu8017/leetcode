<?php
// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution {
    function countHillValley($nums) {
        $compact = [$nums[0]];
        $n = count($nums);
        for ($i = 1; $i < $n; $i++)
            if ($nums[$i] !== $compact[count($compact) - 1]) $compact[] = $nums[$i];
        $ans = 0;
        $m = count($compact);
        for ($i = 1; $i + 1 < $m; $i++)
            if (($compact[$i] > $compact[$i - 1] && $compact[$i] > $compact[$i + 1]) ||
                ($compact[$i] < $compact[$i - 1] && $compact[$i] < $compact[$i + 1]))
                $ans++;
        return $ans;
    }
}
