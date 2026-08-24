<?php
// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

class Solution {
    function validSubstringCount($word1, $word2) {
        $need = array_fill(0, 26, 0);
        $required = 0;
        $m = strlen($word2);
        for ($i = 0; $i < $m; $i++) {
            $idx = ord($word2[$i]) - 97;
            if ($need[$idx] === 0) $required++;
            $need[$idx]++;
        }
        $have = array_fill(0, 26, 0);
        $formed = 0;
        $ans = 0;
        $l = 0;
        $n = strlen($word1);
        for ($r = 0; $r < $n; $r++) {
            $c = ord($word1[$r]) - 97;
            $have[$c]++;
            if ($have[$c] === $need[$c] && $need[$c] > 0) $formed++;
            while ($formed === $required && $l <= $r) {
                $ans += $n - $r;
                $c2 = ord($word1[$l]) - 97;
                if ($have[$c2] === $need[$c2] && $need[$c2] > 0) $formed--;
                $have[$c2]--;
                $l++;
            }
        }
        return $ans;
    }
}
