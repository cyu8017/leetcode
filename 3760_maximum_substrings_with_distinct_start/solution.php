<?php
// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

class Solution {
    function maxDistinct($s) {
        $cnt = array_fill(0, 26, 0);
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $cnt[$idx]++;
            if ($cnt[$idx] === 1) $ans++;
        }
        return $ans;
    }
}
