<?php
// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

class Solution {
    function areSentencesSimilarTwo($sentence1, $sentence2, $similarPairs) {
        if (count($sentence1) !== count($sentence2)) return false;
        $parent = [];
        $find = function ($x) use (&$parent) {
            if (!array_key_exists($x, $parent)) $parent[$x] = $x;
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $unite = function ($a, $b) use (&$find, &$parent) {
            $parent[$find($a)] = $find($b);
        };
        foreach ($similarPairs as $pair) $unite($pair[0], $pair[1]);
        $n = count($sentence1);
        for ($i = 0; $i < $n; $i++) {
            if ($find($sentence1[$i]) !== $find($sentence2[$i])) return false;
        }
        return true;
    }
}
