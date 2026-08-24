<?php
// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution {
    function greatestLetter($s) {
        $lower = array_fill(0, 26, false);
        $upper = array_fill(0, 26, false);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c >= 'a' && $c <= 'z') $lower[ord($c) - 97] = true;
            else $upper[ord($c) - 65] = true;
        }
        for ($i = 25; $i >= 0; --$i)
            if ($lower[$i] && $upper[$i]) return chr(65 + $i);
        return "";
    }
}
