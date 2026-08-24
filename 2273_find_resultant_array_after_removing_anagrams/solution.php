<?php
// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution {
    function removeAnagrams($words) {
        $sig = function($w) {
            $c = array_fill(0, 26, 0);
            $n = strlen($w);
            for ($i = 0; $i < $n; $i++) $c[ord($w[$i]) - 97]++;
            return $c;
        };
        $eq = function($a, $b) {
            for ($i = 0; $i < 26; $i++) if ($a[$i] !== $b[$i]) return false;
            return true;
        };
        $ans = [$words[0]];
        $prev = $sig($words[0]);
        for ($i = 1; $i < count($words); $i++) {
            $cur = $sig($words[$i]);
            if (!$eq($cur, $prev)) {
                $ans[] = $words[$i];
                $prev = $cur;
            }
        }
        return $ans;
    }
}
