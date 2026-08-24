<?php
// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

class Solution {
    function wordSubsets($words1, $words2) {
        $need = array_fill(0, 26, 0);
        foreach ($words2 as $w) {
            $cnt = array_fill(0, 26, 0);
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) $cnt[ord($w[$i]) - 97]++;
            for ($i = 0; $i < 26; $i++) $need[$i] = max($need[$i], $cnt[$i]);
        }
        $ans = [];
        foreach ($words1 as $w) {
            $cnt = array_fill(0, 26, 0);
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) $cnt[ord($w[$i]) - 97]++;
            $ok = true;
            for ($i = 0; $i < 26; $i++) {
                if ($cnt[$i] < $need[$i]) { $ok = false; break; }
            }
            if ($ok) $ans[] = $w;
        }
        return $ans;
    }
}
