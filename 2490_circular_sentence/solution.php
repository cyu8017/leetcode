<?php
// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

class Solution {
    function isCircularSentence($sentence) {
        $n = strlen($sentence);
        if ($sentence[0] !== $sentence[$n - 1]) return false;
        for ($i = 0; $i < $n; $i++) {
            if ($sentence[$i] === ' ' && $sentence[$i - 1] !== $sentence[$i + 1]) return false;
        }
        return true;
    }
}
