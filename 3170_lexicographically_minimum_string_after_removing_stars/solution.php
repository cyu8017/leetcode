<?php
// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

class Solution {
    function clearStars($s) {
        $g = array_fill(0, 26, []);
        $n = strlen($s);
        $rem = array_fill(0, $n, false);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === "*") {
                $rem[$i] = true;
                for ($j = 0; $j < 26; $j++) {
                    if ($g[$j]) {
                        $rem[array_pop($g[$j])] = true;
                        break;
                    }
                }
            } else {
                $g[ord($s[$i]) - 97][] = $i;
            }
        }
        $ans = "";
        for ($i = 0; $i < $n; $i++) if (!$rem[$i]) $ans .= $s[$i];
        return $ans;
    }
}
