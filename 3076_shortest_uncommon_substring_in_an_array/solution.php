<?php
// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

class Solution {
    function shortestSubstrings($arr) {
        $n = count($arr);
        $ans = array_fill(0, $n, "");
        for ($i = 0; $i < $n; $i++) {
            $s = $arr[$i];
            $m = strlen($s);
            for ($j = 1; $j <= $m && $ans[$i] === ""; $j++) {
                for ($l = 0; $l <= $m - $j; $l++) {
                    $sub = substr($s, $l, $j);
                    if ($ans[$i] === "" || $ans[$i] > $sub) {
                        $ok = true;
                        for ($k = 0; $k < $n; $k++) {
                            if ($k !== $i && str_contains($arr[$k], $sub)) { $ok = false; break; }
                        }
                        if ($ok) $ans[$i] = $sub;
                    }
                }
            }
        }
        return $ans;
    }
}
