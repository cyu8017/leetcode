<?php
// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

class TrieNode {
    /** @var array<string, TrieNode> */
    public $children = [];
    public $wordCount = 0;
    public $prefixCount = 0;
}

class Trie {
    private $root;

    function __construct() {
        $this->root = new TrieNode();
    }

    /**
     * @param String $word
     * @return NULL
     */
    function insert($word) {
        $node = $this->root;
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $ch = $word[$i];
            if (!isset($node->children[$ch])) {
                $node->children[$ch] = new TrieNode();
            }
            $node = $node->children[$ch];
            $node->prefixCount++;
        }
        $node->wordCount++;
    }

    /**
     * @param String $word
     * @return Integer
     */
    function countWordsEqualTo($word) {
        $node = $this->find($word);
        return $node !== null ? $node->wordCount : 0;
    }

    /**
     * @param String $prefix
     * @return Integer
     */
    function countWordsStartingWith($prefix) {
        $node = $this->find($prefix);
        return $node !== null ? $node->prefixCount : 0;
    }

    /**
     * @param String $word
     * @return NULL
     */
    function erase($word) {
        $node = $this->root;
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $node = $node->children[$word[$i]];
            $node->prefixCount--;
        }
        $node->wordCount--;
    }

    private function find($text) {
        $node = $this->root;
        $len = strlen($text);
        for ($i = 0; $i < $len; $i++) {
            $ch = $text[$i];
            if (!isset($node->children[$ch])) {
                return null;
            }
            $node = $node->children[$ch];
        }
        return $node;
    }
}
