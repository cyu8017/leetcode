<?php
// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution {
    function countConsistentStrings($allowed, $words) {
        $a = array_flip(str_split($allowed));
        $ans = 0;
        foreach ($words as $w) {
            $ok = true;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                if (!isset($a[$w[$i]])) { $ok = false; break; }
            }
            if ($ok) $ans++;
        }
        return $ans;
    }
}
