<?php
// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function possiblyEquals($s1, $s2) {
        $memo = [];
        $isDigit = function ($c) { return $c >= '0' && $c <= '9'; };
        $dfs = null;
        $dfs = function ($i, $j, $diff) use (&$dfs, &$memo, $s1, $s2, $isDigit) {
            $key = $i . "," . $j . "," . $diff;
            if (isset($memo[$key])) return $memo[$key];
            $n = strlen($s1);
            $m = strlen($s2);
            if ($i === $n && $j === $m) { $memo[$key] = $diff === 0; return $diff === 0; }
            $res = false;
            if ($diff === 0 && $i < $n && $j < $m && !$isDigit($s1[$i]) && !$isDigit($s2[$j])) {
                if ($s1[$i] === $s2[$j]) $res = $dfs($i + 1, $j + 1, 0);
            } else if ($diff > 0 && $i < $n && !$isDigit($s1[$i])) {
                $res = $dfs($i + 1, $j, $diff - 1);
            } else if ($diff < 0 && $j < $m && !$isDigit($s2[$j])) {
                $res = $dfs($i, $j + 1, $diff + 1);
            }
            if (!$res && $i < $n && $isDigit($s1[$i])) {
                $val = 0;
                for ($p = $i; $p < $n && $isDigit($s1[$p]); $p++) {
                    $val = $val * 10 + (ord($s1[$p]) - 48);
                    if ($dfs($p + 1, $j, $diff + $val)) { $res = true; break; }
                }
            }
            if (!$res && $j < $m && $isDigit($s2[$j])) {
                $val = 0;
                for ($p = $j; $p < $m && $isDigit($s2[$p]); $p++) {
                    $val = $val * 10 + (ord($s2[$p]) - 48);
                    if ($dfs($i, $p + 1, $diff - $val)) { $res = true; break; }
                }
            }
            $memo[$key] = $res;
            return $res;
        };
        return $dfs(0, 0, 0);
    }
}
