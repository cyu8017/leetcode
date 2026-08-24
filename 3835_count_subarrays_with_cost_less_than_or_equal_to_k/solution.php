<?php
// LeetCode 3835 - Count Subarrays With Cost Less Than or Equal to K
// https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/

class Solution {
    function countSubarrays($nums, $k) {
        $ans = 0;
        $q1 = [];
        $q2 = [];
        $l = 0;
        $n = count($nums);
        for ($r = 0; $r < $n; $r++) {
            $x = $nums[$r];
            while (count($q1) && $nums[$q1[count($q1) - 1]] <= $x) array_pop($q1);
            while (count($q2) && $nums[$q2[count($q2) - 1]] >= $x) array_pop($q2);
            $q1[] = $r;
            $q2[] = $r;
            while ($l < $r && ($nums[$q1[0]] - $nums[$q2[0]]) * ($r - $l + 1) > $k) {
                $l++;
                if ($q1[0] < $l) array_shift($q1);
                if ($q2[0] < $l) array_shift($q2);
            }
            $ans += $r - $l + 1;
        }
        return $ans;
    }
}
