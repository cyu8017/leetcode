<?php
// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

class Solution {
    /**
     * @param String $sentence1
     * @param String $sentence2
     * @return Boolean
     */
    function areSentencesSimilar($sentence1, $sentence2) {
        $words1 = preg_split('/\s+/', $sentence1, -1, PREG_SPLIT_NO_EMPTY);
        $words2 = preg_split('/\s+/', $sentence2, -1, PREG_SPLIT_NO_EMPTY);
        $n1 = count($words1);
        $n2 = count($words2);

        $i = 0;
        while ($i < $n1 && $i < $n2 && $words1[$i] === $words2[$i]) {
            $i++;
        }
        if ($i === $n1 || $i === $n2) {
            return true;
        }

        $j1 = $n1 - 1;
        $j2 = $n2 - 1;
        while ($j1 >= $i && $j2 >= $i && $words1[$j1] === $words2[$j2]) {
            $j1--;
            $j2--;
        }
        return $j1 < $i || $j2 < $i;
    }
}
