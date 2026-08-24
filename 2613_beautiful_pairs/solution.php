<?php
// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

class Solution {
    function beautifulPair($nums1, $nums2) {
        $n = count($nums1);
        $best = PHP_INT_MAX;
        $ans = [0, 1];
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $d = abs($nums1[$i] - $nums1[$j]) + abs($nums2[$i] - $nums2[$j]);
                if ($d < $best || ($d === $best && ($i < $ans[0] || ($i === $ans[0] && $j < $ans[1])))) {
                    $best = $d;
                    $ans = [$i, $j];
                }
            }
        }
        return $ans;
    }
}
