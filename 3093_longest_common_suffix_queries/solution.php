<?php
// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

class Trie {
    public $children;
    public $length;
    public $idx;
    function __construct() {
        $this->children = array_fill(0, 26, null);
        $this->length = 1 << 30;
        $this->idx = 1 << 30;
    }
}

class Solution {
    function stringIndices($wordsContainer, $wordsQuery) {
        $trie = new Trie();
        for ($i = 0; $i < count($wordsContainer); $i++) $this->insert($trie, $wordsContainer[$i], $i);
        $ans = [];
        for ($i = 0; $i < count($wordsQuery); $i++) $ans[$i] = $this->query($trie, $wordsQuery[$i]);
        return $ans;
    }
    function insert($t, $w, $i) {
        $node = $t;
        $len = strlen($w);
        if ($node->length > $len) {
            $node->length = $len;
            $node->idx = $i;
        }
        for ($k = $len - 1; $k >= 0; $k--) {
            $id = ord($w[$k]) - 97;
            if ($node->children[$id] === null) $node->children[$id] = new Trie();
            $node = $node->children[$id];
            if ($node->length > $len) {
                $node->length = $len;
                $node->idx = $i;
            }
        }
    }
    function query($t, $w) {
        $node = $t;
        for ($k = strlen($w) - 1; $k >= 0; $k--) {
            $id = ord($w[$k]) - 97;
            if ($node->children[$id] === null) break;
            $node = $node->children[$id];
        }
        return $node->idx;
    }
}
