<?php
// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

class Solution {
    function finalString($s) {
        $b = '';
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === 'i') $b = strrev($b);
            else $b .= $s[$i];
        }
        return $b;
    }
}
