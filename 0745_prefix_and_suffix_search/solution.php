<?php
// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter {
    private $lookup = [];

    function __construct($words) {
        $this->lookup = [];
        for ($index = 0; $index < count($words); $index++) {
            $word = $words[$index];
            $size = strlen($word);
            for ($i = 0; $i <= $size; $i++) {
                for ($j = 0; $j <= $size; $j++) {
                    $this->lookup[substr($word, 0, $i) . '#' . substr($word, $j)] = $index;
                }
            }
        }
    }

    function f($pref, $suff) {
        $key = $pref . '#' . $suff;
        return array_key_exists($key, $this->lookup) ? $this->lookup[$key] : -1;
    }
}
