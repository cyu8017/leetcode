<?php
// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution {
    function minAddToMakeValid($s) {
        $openNeed = 0;
        $closeNeed = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === "(") $closeNeed++;
            elseif ($closeNeed > 0) $closeNeed--;
            else $openNeed++;
        }
        return $openNeed + $closeNeed;
    }
}
