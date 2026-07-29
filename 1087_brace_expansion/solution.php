<?php
// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function expand($s) {
        $groups = [];
        $i = 0;
        $n = strlen($s);
        while ($i < $n) {
            if ($s[$i] === "{") {
                $j = strpos($s, "}", $i);
                $parts = explode(",", substr($s, $i + 1, $j - $i - 1));
                sort($parts);
                $groups[] = $parts;
                $i = $j + 1;
            } else {
                $groups[] = [$s[$i]];
                $i++;
            }
        }
        $ans = [""];
        foreach ($groups as $group) {
            $next = [];
            foreach ($ans as $prefix) {
                foreach ($group as $ch) {
                    $next[] = $prefix . $ch;
                }
            }
            $ans = $next;
        }
        return $ans;
    }
}
