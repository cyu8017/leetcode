<?php
// LeetCode 3460 - Longest Common Prefix After at Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

class Solution {
    function longestCommonPrefix($s, $t) {
        $i = 0;
        $j = 0;
        $removed = false;
        $sn = strlen($s);
        $tn = strlen($t);
        while ($i < $sn && $j < $tn) {
            if ($s[$i] === $t[$j]) {
                $i++;
                $j++;
                continue;
            }
            if ($removed) break;
            $removed = true;
            $i++;
        }
        return $j;
    }
}
