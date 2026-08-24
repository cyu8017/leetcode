<?php
// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

class Solution {
    function stableMountains($height, $threshold) {
        $ans = [];
        $n = count($height);
        for ($i = 1; $i < $n; $i++) {
            if ($height[$i - 1] > $threshold) $ans[] = $i;
        }
        return $ans;
    }
}
