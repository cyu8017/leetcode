<?php
// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution {
    /**
     * @param String $seq
     * @return Integer[]
     */
    function maxDepthAfterSplit($seq) {
        $ans = [];
        $depth = 0;
        $n = strlen($seq);
        for ($i = 0; $i < $n; $i++) {
            if ($seq[$i] === '(') {
                $ans[] = $depth % 2;
                $depth++;
            } else {
                $depth--;
                $ans[] = $depth % 2;
            }
        }
        return $ans;
    }
}
