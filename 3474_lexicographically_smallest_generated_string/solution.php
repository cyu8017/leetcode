<?php
// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

class Solution {
    function generateString($str1, $str2) {
        $n = strlen($str1);
        $m = strlen($str2);
        $L = $n + $m - 1;
        $ans = array_fill(0, $L, "?");
        for ($i = 0; $i < $n; $i++) {
            if ($str1[$i] === "T") {
                for ($j = 0; $j < $m; $j++) {
                    if ($ans[$i + $j] !== "?" && $ans[$i + $j] !== $str2[$j]) return "";
                    $ans[$i + $j] = $str2[$j];
                }
            }
        }
        for ($i = 0; $i < $L; $i++) if ($ans[$i] === "?") $ans[$i] = "a";
        for ($i = 0; $i < $n; $i++) {
            if ($str1[$i] === "F") {
                $match = true;
                for ($j = 0; $j < $m; $j++) if ($ans[$i + $j] !== $str2[$j]) { $match = false; break; }
                if ($match) {
                    $changed = false;
                    for ($j = $m - 1; $j >= 0; $j--) {
                        $pos = $i + $j;
                        $forced = false;
                        for ($t = 0; $t < $n; $t++) {
                            if ($str1[$t] === "T" && $pos >= $t && $pos < $t + $m) { $forced = true; break; }
                        }
                        if (!$forced) {
                            $ans[$pos] = "b";
                            $changed = true;
                            break;
                        }
                    }
                    if (!$changed) return "";
                }
            }
        }
        for ($i = 0; $i < $n; $i++) {
            $match = true;
            for ($j = 0; $j < $m; $j++) if ($ans[$i + $j] !== $str2[$j]) { $match = false; break; }
            if ($str1[$i] === "T" && !$match) return "";
            if ($str1[$i] === "F" && $match) return "";
        }
        return implode("", $ans);
    }
}
