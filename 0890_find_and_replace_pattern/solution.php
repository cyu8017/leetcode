<?php
// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

class Solution {
    function findAndReplacePattern($words, $pattern) {
        $match = function ($w, $p) {
            $m1 = [];
            $m2 = [];
            $n = strlen($w);
            for ($i = 0; $i < $n; $i++) {
                $a = $w[$i];
                $b = $p[$i];
                if (!array_key_exists($a, $m1)) $m1[$a] = $b;
                if (!array_key_exists($b, $m2)) $m2[$b] = $a;
                if ($m1[$a] !== $b || $m2[$b] !== $a) return false;
            }
            return true;
        };
        $ans = [];
        foreach ($words as $w) {
            if ($match($w, $pattern)) $ans[] = $w;
        }
        return $ans;
    }
}
