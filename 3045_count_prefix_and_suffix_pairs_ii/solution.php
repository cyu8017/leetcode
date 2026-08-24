<?php
// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

class Node {
    public $children = [];
    public $cnt = 0;
}

class Solution {
    function countPrefixSuffixPairs($words) {
        $trie = new Node();
        $ans = 0;
        foreach ($words as $s) {
            $node = $trie;
            $m = strlen($s);
            for ($i = 0; $i < $m; $i++) {
                $p = ord($s[$i]) * 32 + ord($s[$m - $i - 1]);
                if (!isset($node->children[$p])) $node->children[$p] = new Node();
                $node = $node->children[$p];
                $ans += $node->cnt;
            }
            $node->cnt++;
        }
        return $ans;
    }
}
