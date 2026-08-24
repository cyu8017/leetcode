<?php
// LeetCode 3158 - Find the XOR of Numbers Which Appear Twice
// https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

class Solution {
    function duplicateNumbersXOR($nums) {
        $cnt = array_fill(0, 51, 0);
        $ans = 0;
        foreach ($nums as $x) {
            $cnt[$x]++;
            if ($cnt[$x] === 2) $ans ^= $x;
        }
        return $ans;
    }
}
