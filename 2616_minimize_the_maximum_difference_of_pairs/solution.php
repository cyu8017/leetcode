<?php
// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

class Solution {
    function minimizeMax($nums, $p) {
        sort($nums);
        $lo = 0;
        $hi = $nums[count($nums) - 1] - $nums[0];
        $ok = function($d) use ($nums, $p) {
            $cnt = 0;
            $n = count($nums);
            for ($i = 0; $i + 1 < $n; ) {
                if ($nums[$i + 1] - $nums[$i] <= $d) {
                    $cnt++;
                    $i += 2;
                } else $i++;
            }
            return $cnt >= $p;
        };
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
