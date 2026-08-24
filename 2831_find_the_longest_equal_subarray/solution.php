<?php
// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

class Solution {
    function longestEqualSubarray($nums, $k) {
        $pos = [];
        for ($i = 0; $i < count($nums); $i++) $pos[$nums[$i]][] = $i;
        $ans = 0;
        foreach ($pos as $p) {
            $left = 0;
            for ($right = 0; $right < count($p); $right++) {
                while ($p[$right] - $p[$left] - ($right - $left) > $k) $left++;
                $ans = max($ans, $right - $left + 1);
            }
        }
        return $ans;
    }
}
