<?php
// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution {
    function findArray($pref) {
        $ans = array_fill(0, count($pref), 0);
        $ans[0] = $pref[0];
        for ($i = 1; $i < count($pref); $i++) $ans[$i] = $pref[$i] ^ $pref[$i - 1];
        return $ans;
    }
}
