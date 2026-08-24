<?php
// LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
// https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

class Solution {
    function isVowel($c) {
        return $c === 'a' || $c === 'e' || $c === 'i' || $c === 'o' || $c === 'u';
    }

    function atLeast($word, $k) {
        $cnt = [];
        $cons = 0;
        $l = 0;
        $ans = 0;
        $n = strlen($word);
        for ($r = 0; $r < $n; $r++) {
            $c = $word[$r];
            if ($this->isVowel($c)) $cnt[$c] = ($cnt[$c] ?? 0) + 1;
            else $cons++;
            while (count($cnt) === 5 && $cons >= $k) {
                $ans += $n - $r;
                $c2 = $word[$l];
                if ($this->isVowel($c2)) {
                    $nv = $cnt[$c2] - 1;
                    if ($nv === 0) unset($cnt[$c2]);
                    else $cnt[$c2] = $nv;
                } else $cons--;
                $l++;
            }
        }
        return $ans;
    }

    function countOfSubstrings($word, $k) {
        return $this->atLeast($word, $k) - $this->atLeast($word, $k + 1);
    }
}
