<?php
// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

class StreamChecker {
    private $trie = [];
    private $stream = [];

    /**
     * @param String[] $words
     */
    function __construct($words) {
        foreach ($words as $word) {
            $node = &$this->trie;
            for ($i = strlen($word) - 1; $i >= 0; $i--) {
                $ch = $word[$i];
                if (!isset($node[$ch])) {
                    $node[$ch] = [];
                }
                $node = &$node[$ch];
            }
            $node['$'] = true;
            unset($node);
        }
    }

    /**
     * @param String $letter
     * @return Boolean
     */
    function query($letter) {
        $this->stream[] = $letter;
        $node = $this->trie;
        for ($i = count($this->stream) - 1; $i >= 0; $i--) {
            if (isset($node['$'])) {
                return true;
            }
            $ch = $this->stream[$i];
            if (!isset($node[$ch])) {
                return false;
            }
            $node = $node[$ch];
        }
        return isset($node['$']);
    }
}
