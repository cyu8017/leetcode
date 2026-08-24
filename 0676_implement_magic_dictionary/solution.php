<?php
// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

class MagicDictionary {
    private $words = [];

    function __construct() {}

    function buildDict($dictionary) {
        $this->words = $dictionary;
    }

    function search($searchWord) {
        foreach ($this->words as $word) {
            if (strlen($word) !== strlen($searchWord)) continue;
            $diff = 0;
            for ($i = 0; $i < strlen($word); ++$i) {
                if ($word[$i] !== $searchWord[$i]) ++$diff;
            }
            if ($diff === 1) return true;
        }
        return false;
    }
}
