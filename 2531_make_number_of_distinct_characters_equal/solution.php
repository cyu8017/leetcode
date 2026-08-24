<?php
// LeetCode 2531 - Make Number of Distinct Characters Equal
// https://leetcode.com/problems/make-number-of-distinct-characters-equal/

class Solution {
    function isItPossible($word1, $word2) {
        $c1 = array_fill(0, 26, 0);
        $c2 = array_fill(0, 26, 0);
        $n1 = strlen($word1);
        $n2 = strlen($word2);
        for ($i = 0; $i < $n1; $i++) $c1[ord($word1[$i]) - 97]++;
        for ($i = 0; $i < $n2; $i++) $c2[ord($word2[$i]) - 97]++;
        $d1 = 0;
        $d2 = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($c1[$i] > 0) $d1++;
            if ($c2[$i] > 0) $d2++;
        }
        for ($a = 0; $a < 26; $a++) {
            if ($c1[$a] === 0) continue;
            for ($b = 0; $b < 26; $b++) {
                if ($c2[$b] === 0) continue;
                $nd1 = $d1;
                $nd2 = $d2;
                if ($a === $b) {
                    if ($nd1 === $nd2) return true;
                    continue;
                }
                if ($c1[$a] === 1) $nd1--;
                if ($c1[$b] === 0) $nd1++;
                if ($c2[$b] === 1) $nd2--;
                if ($c2[$a] === 0) $nd2++;
                if ($nd1 === $nd2) return true;
            }
        }
        return false;
    }
}
