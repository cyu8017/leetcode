<?php
// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

class Solution {
    function findTheString($lcp) {
        $n = count($lcp);
        $s = array_fill(0, $n, 0);
        $c = 97;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] !== 0) continue;
            if ($c > 122) return "";
            $s[$i] = $c;
            for ($j = $i + 1; $j < $n; $j++) {
                if ($lcp[$i][$j] > 0) $s[$j] = $c;
            }
            $c++;
        }
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $n - 1; $j >= 0; $j--) {
                $v = 0;
                if ($s[$i] === $s[$j]) {
                    $v = 1;
                    if ($i + 1 < $n && $j + 1 < $n) $v += $lcp[$i + 1][$j + 1];
                }
                if ($lcp[$i][$j] !== $v) return "";
            }
        }
        $out = '';
        for ($i = 0; $i < $n; $i++) $out .= chr($s[$i]);
        return $out;
    }
}
