<?php
// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

class Solution {
    function minimizedStringLength($s) {
        $seen = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $seen[$s[$i]] = true;
        return count($seen);
    }
}
