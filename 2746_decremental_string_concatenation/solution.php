<?php
// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

class Solution {
    public $words;
    public $memo;
    public $n;
    function minimizeConcatenatedLength($words) {
        $this->words = $words;
        $this->n = count($words);
        $this->memo = [];
        $w0 = $words[0];
        return strlen($w0) + $this->dfs(1, $w0[0], $w0[strlen($w0) - 1]);
    }
    function dfs($i, $first, $last) {
        if ($i === $this->n) return 0;
        $key = $i . ',' . $first . ',' . $last;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $w = $this->words[$i];
        $wf = $w[0];
        $wl = $w[strlen($w) - 1];
        $add1 = strlen($w) - ($last === $wf ? 1 : 0);
        $add2 = strlen($w) - ($wl === $first ? 1 : 0);
        $a = $add1 + $this->dfs($i + 1, $first, $wl);
        $b = $add2 + $this->dfs($i + 1, $wf, $last);
        return $this->memo[$key] = min($a, $b);
    }
}
