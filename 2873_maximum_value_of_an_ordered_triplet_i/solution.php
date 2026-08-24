<?php
// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

class Solution {
    function maximumTripletValue($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                for ($k = $j + 1; $k < $n; $k++) {
                    $cand = ($nums[$i] - $nums[$j]) * $nums[$k];
                    if ($cand > $ans) $ans = $cand;
                }
        return $ans;
    }
}
