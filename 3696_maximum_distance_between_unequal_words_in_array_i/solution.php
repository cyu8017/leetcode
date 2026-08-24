<?php
// LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

class Solution {
    function maxDistance($words) {
        $n = count($words);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($words[$i] !== $words[0]) $ans = max($ans, $i + 1);
            if ($words[$i] !== $words[$n - 1]) $ans = max($ans, $n - $i);
        }
        return $ans;
    }
}
