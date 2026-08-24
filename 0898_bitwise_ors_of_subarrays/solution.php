<?php
// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

class Solution {
    function subarrayBitwiseORs($arr) {
        $ans = [];
        $cur = [];
        foreach ($arr as $x) {
            $nxt = [$x => true];
            foreach ($cur as $y => $_) $nxt[$x | $y] = true;
            $cur = $nxt;
            foreach ($cur as $v => $_) $ans[$v] = true;
        }
        return count($ans);
    }
}
