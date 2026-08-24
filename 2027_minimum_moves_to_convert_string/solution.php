<?php
// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minimumMoves($s) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; ) {
            if ($s[$i] === 'X') { $ans++; $i += 3; }
            else $i++;
        }
        return $ans;
    }
}
