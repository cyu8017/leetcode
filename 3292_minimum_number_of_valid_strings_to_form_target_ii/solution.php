<?php
// LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

class TrieNode3292 {
    public $next;
    function __construct() {
        $this->next = array_fill(0, 26, null);
    }
}

class Solution {
    function minValidStrings($words, $target) {
        $n = strlen($target);
        $inf = 1000000000;
        $dp = array_fill(0, $n + 1, $inf);
        $dp[0] = 0;
        $root = new TrieNode3292();
        foreach ($words as $w) {
            $cur = $root;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) {
                $ci = ord($w[$i]) - 97;
                if ($cur->next[$ci] === null) $cur->next[$ci] = new TrieNode3292();
                $cur = $cur->next[$ci];
            }
        }
        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] === $inf) continue;
            $cur = $root;
            for ($j = $i; $j < $n; $j++) {
                $ci = ord($target[$j]) - 97;
                if ($cur->next[$ci] === null) break;
                $cur = $cur->next[$ci];
                if ($dp[$i] + 1 < $dp[$j + 1]) $dp[$j + 1] = $dp[$i] + 1;
            }
        }
        return $dp[$n] === $inf ? -1 : $dp[$n];
    }
}
