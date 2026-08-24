<?php
// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class TrieNode {
    public $child;
    public $cnt = 0;
    function __construct() {
        $this->child = array_fill(0, 26, null);
    }
}

class Solution {
    function sumPrefixScores($words) {
        $root = new TrieNode();
        foreach ($words as $w) {
            $cur = $root;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $c = ord($w[$i]) - 97;
                if ($cur->child[$c] === null) $cur->child[$c] = new TrieNode();
                $cur = $cur->child[$c];
                $cur->cnt++;
            }
        }
        $n = count($words);
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $cur = $root;
            $sum = 0;
            $w = $words[$i];
            $len = strlen($w);
            for ($j = 0; $j < $len; $j++) {
                $cur = $cur->child[ord($w[$j]) - 97];
                $sum += $cur->cnt;
            }
            $ans[$i] = $sum;
        }
        return $ans;
    }
}
