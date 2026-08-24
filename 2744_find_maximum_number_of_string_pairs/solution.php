<?php
// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

class Solution {
    function maximumNumberOfStringPairs($words) {
        $freq = [];
        $ans = 0;
        foreach ($words as $w) {
            $rev = strrev($w);
            $c = $freq[$rev] ?? 0;
            if ($c > 0) {
                $ans++;
                $freq[$rev] = $c - 1;
            } else {
                $freq[$w] = ($freq[$w] ?? 0) + 1;
            }
        }
        return $ans;
    }
}
