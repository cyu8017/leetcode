<?php
// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution {
    /**
     * @param Integer[] $colors
     * @return Integer
     */
    function maxDistance($colors) {
        $n = count($colors);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($colors[$i] !== $colors[0]) $ans = max($ans, $i);
            if ($colors[$i] !== $colors[$n - 1]) $ans = max($ans, $n - 1 - $i);
        }
        return $ans;
    }
}
