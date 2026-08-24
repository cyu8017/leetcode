<?php
// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

class Solution {
    function boldWords($words, $s) {
        $n = strlen($s);
        $bold = array_fill(0, $n, false);
        foreach ($words as $word) {
            $start = strpos($s, $word);
            while ($start !== false) {
                $wlen = strlen($word);
                for ($i = $start; $i < $start + $wlen; $i++) $bold[$i] = true;
                $start = strpos($s, $word, $start + 1);
            }
        }
        $parts = '';
        $i2 = 0;
        while ($i2 < $n) {
            if ($bold[$i2]) {
                $parts .= '**';
                while ($i2 < $n && $bold[$i2]) $parts .= $s[$i2++];
                $parts .= '**';
            } else $parts .= $s[$i2++];
        }
        return $parts;
    }
}
