<?php
// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

class Solution {
    private $n;
    private $words;
    private $tm;
    private $keys;

    private function calc($s, $t) {
        $m = min(strlen($s), strlen($t));
        for ($k = 0; $k < $m; $k++) if ($s[$k] !== $t[$k]) return $k;
        return $m;
    }

    private function addKey($x) {
        if (!isset($this->tm[$x])) {
            $this->tm[$x] = 0;
            $lo = 0;
            $hi = count($this->keys);
            while ($lo < $hi) {
                $mid = ($lo + $hi) >> 1;
                if ($this->keys[$mid] < $x) $lo = $mid + 1;
                else $hi = $mid;
            }
            array_splice($this->keys, $lo, 0, [$x]);
        }
        $this->tm[$x]++;
    }

    private function remKey($x) {
        $c = $this->tm[$x] - 1;
        if ($c === 0) {
            unset($this->tm[$x]);
            $ix = array_search($x, $this->keys, true);
            if ($ix !== false) array_splice($this->keys, $ix, 1);
        } else $this->tm[$x] = $c;
    }

    private function add($i, $j) {
        if ($i >= 0 && $i < $this->n && $j >= 0 && $j < $this->n)
            $this->addKey($this->calc($this->words[$i], $this->words[$j]));
    }

    private function remove($i, $j) {
        if ($i >= 0 && $i < $this->n && $j >= 0 && $j < $this->n)
            $this->remKey($this->calc($this->words[$i], $this->words[$j]));
    }

    function longestCommonPrefix($words) {
        $this->n = count($words);
        $this->words = $words;
        $this->tm = [];
        $this->keys = [];
        for ($i = 0; $i + 1 < $this->n; $i++) $this->add($i, $i + 1);
        $ans = array_fill(0, $this->n, 0);
        for ($i = 0; $i < $this->n; $i++) {
            $this->remove($i, $i + 1);
            $this->remove($i - 1, $i);
            $this->add($i - 1, $i + 1);
            if (count($this->keys) && $this->keys[count($this->keys) - 1] > 0)
                $ans[$i] = $this->keys[count($this->keys) - 1];
            $this->remove($i - 1, $i + 1);
            $this->add($i - 1, $i);
            $this->add($i, $i + 1);
        }
        return $ans;
    }
}
