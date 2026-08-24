<?php
// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

class Solution {
    function checkValidString($s) {
        $lo = 0;
        $hi = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; ++$i) {
            $ch = $s[$i];
            if ($ch === "(") {
                ++$lo;
                ++$hi;
            } elseif ($ch === ")") {
                $lo = max($lo - 1, 0);
                --$hi;
                if ($hi < 0) return false;
            } else {
                $lo = max($lo - 1, 0);
                ++$hi;
            }
        }
        return $lo === 0;
    }
}
