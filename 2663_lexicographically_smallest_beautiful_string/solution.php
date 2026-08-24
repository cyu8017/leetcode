<?php
// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

class Solution {
    function smallestBeautifulString($s, $k) {
        $n = strlen($s);
        $b = str_split($s);
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($code = ord($b[$i]) + 1; $code < 97 + $k; $code++) {
                $c = chr($code);
                if (($i > 0 && $c === $b[$i - 1]) || ($i > 1 && $c === $b[$i - 2])) continue;
                $b[$i] = $c;
                for ($j = $i + 1; $j < $n; $j++) {
                    for ($nc = 97; $nc < 97 + $k; $nc++) {
                        $ch = chr($nc);
                        if (($j > 0 && $ch === $b[$j - 1]) || ($j > 1 && $ch === $b[$j - 2])) continue;
                        $b[$j] = $ch;
                        break;
                    }
                }
                return implode("", $b);
            }
        }
        return "";
    }
}
