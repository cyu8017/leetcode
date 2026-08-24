<?php
// LeetCode 2124 - Check if All A's Appears Before All B's
// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function checkString($s) {
        $seenB = false;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === 'b') $seenB = true;
            else if ($seenB) return false;
        }
        return true;
    }
}
