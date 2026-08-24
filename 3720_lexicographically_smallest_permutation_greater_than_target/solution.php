<?php
// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

class Solution {
    function lexGreaterPermutation($s, $target) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $ans = array_fill(0, $n, '');
        $dfs = function($pos, $greater) use (&$dfs, &$cnt, &$ans, $n, $target) {
            if ($pos === $n) return $greater;
            $start = $greater ? 0 : (ord($target[$pos]) - 97);
            for ($c = $start; $c < 26; $c++) {
                if ($cnt[$c] === 0) continue;
                $cnt[$c]--;
                $ans[$pos] = chr(97 + $c);
                $ng = $greater || $c > (ord($target[$pos]) - 97);
                if ($dfs($pos + 1, $ng)) return true;
                $cnt[$c]++;
            }
            return false;
        };
        if ($dfs(0, false)) return implode('', $ans);
        return "";
    }
}
