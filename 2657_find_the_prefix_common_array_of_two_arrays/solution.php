<?php
// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution {
    function findThePrefixCommonArray($A, $B) {
        $n = count($A);
        $seenA = array_fill(0, $n + 1, false);
        $seenB = array_fill(0, $n + 1, false);
        $ans = array_fill(0, $n, 0);
        $common = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($seenB[$A[$i]]) $common++;
            $seenA[$A[$i]] = true;
            if ($seenA[$B[$i]]) $common++;
            $seenB[$B[$i]] = true;
            $ans[$i] = $common;
        }
        return $ans;
    }
}
