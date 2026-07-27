<?php
// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

class Solution {
    function countDistinct($s) {
        $root = [];
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $node =& $root;
            for ($j = $i; $j < $n; $j++) {
                $c = $s[$j];
                if (!isset($node[$c])) {
                    $node[$c] = [];
                    $ans++;
                }
                $node =& $node[$c];
            }
            unset($node);
        }
        return $ans;
    }
}
