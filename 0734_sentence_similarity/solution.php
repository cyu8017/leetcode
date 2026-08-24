<?php
// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

class Solution {
    function areSentencesSimilar($sentence1, $sentence2, $similarPairs) {
        if (count($sentence1) !== count($sentence2)) return false;
        $pairs = [];
        foreach ($similarPairs as $pair) {
            $pairs[$pair[0] . '#' . $pair[1]] = true;
            $pairs[$pair[1] . '#' . $pair[0]] = true;
        }
        $n = count($sentence1);
        for ($i = 0; $i < $n; $i++) {
            if ($sentence1[$i] !== $sentence2[$i] && !isset($pairs[$sentence1[$i] . '#' . $sentence2[$i]])) return false;
        }
        return true;
    }
}
