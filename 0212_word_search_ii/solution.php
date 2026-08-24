<?php
// LeetCode 0212 - Word Search II
// https://leetcode.com/problems/word-search-ii/

class TrieNode {
    public $children = [];
    public $word = null;
}

class Solution {
    function findWords($board, $words) {
        $root = new TrieNode();
        foreach ($words as $word) {
            $node = $root;
            for ($i = 0; $i < strlen($word); $i++) {
                $char = $word[$i];
                if (!isset($node->children[$char])) {
                    $node->children[$char] = new TrieNode();
                }
                $node = $node->children[$char];
            }
            $node->word = $word;
        }

        $rows = count($board);
        $cols = count($board[0]);
        $result = [];

        $dfs = function ($r, $c, $node) use (&$dfs, &$board, &$result, $rows, $cols) {
            $char = $board[$r][$c];
            if (!isset($node->children[$char])) {
                return;
            }
            $next = $node->children[$char];
            if ($next->word !== null) {
                $result[] = $next->word;
                $next->word = null;
            }
            $board[$r][$c] = '#';
            $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
            foreach ($dirs as [$dr, $dc]) {
                $nr = $r + $dr;
                $nc = $c + $dc;
                if ($nr >= 0 && $nr < $rows && $nc >= 0 && $nc < $cols && $board[$nr][$nc] !== '#') {
                    $dfs($nr, $nc, $next);
                }
            }
            $board[$r][$c] = $char;
            if (empty($next->children)) {
                unset($node->children[$char]);
            }
        };

        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                $dfs($r, $c, $root);
            }
        }
        return $result;
    }
}
