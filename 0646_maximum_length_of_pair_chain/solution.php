<?php
// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution {
    function findLongestChain($pairs) {
        usort($pairs, function($a, $b) { return $a[1] <=> $b[1]; });
        $length = 0;
        $currentEnd = PHP_INT_MIN;
        foreach ($pairs as $pair) {
            if ($pair[0] > $currentEnd) {
                ++$length;
                $currentEnd = $pair[1];
            }
        }
        return $length;
    }
}
