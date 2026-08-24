<?php
// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution {
    function minLength($s) {
        $st = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $last = count($st) ? $st[count($st) - 1] : null;
            if (count($st) && (($last === "A" && $c === "B") || ($last === "C" && $c === "D"))) {
                array_pop($st);
            } else {
                $st[] = $c;
            }
        }
        return count($st);
    }
}
