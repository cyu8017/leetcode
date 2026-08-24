<?php
// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

class Solution {
    function maxSubstrings($word) {
        $ans = 0;
        $first = [];
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $c = $word[$i];
            if (!isset($first[$c])) $first[$c] = $i;
            else if ($i - $first[$c] + 1 >= 4) {
                $ans++;
                $first = [];
            }
        }
        return $ans;
    }
}
