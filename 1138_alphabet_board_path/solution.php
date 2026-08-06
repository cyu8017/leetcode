<?php
// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

class Solution {
    /**
     * @param String $target
     * @return String
     */
    function alphabetBoardPath($target) {
        $row = 0;
        $col = 0;
        $ans = '';
        $n = strlen($target);
        for ($i = 0; $i < $n; $i++) {
            $code = ord($target[$i]) - 97;
            $r = intdiv($code, 5);
            $c = $code % 5;
            while ($row > $r) { $ans .= 'U'; $row--; }
            while ($col > $c) { $ans .= 'L'; $col--; }
            while ($col < $c) { $ans .= 'R'; $col++; }
            while ($row < $r) { $ans .= 'D'; $row++; }
            $ans .= '!';
        }
        return $ans;
    }
}
