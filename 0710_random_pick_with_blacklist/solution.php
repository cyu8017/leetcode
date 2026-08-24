<?php
// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

class Solution {
    private $size;
    private $mapping;

    function __construct($n, $blacklist) {
        $this->size = $n - count($blacklist);
        $this->mapping = [];
        $black = [];
        foreach ($blacklist as $b) $black[$b] = true;
        $white = $this->size;
        foreach ($blacklist as $b) {
            if ($b < $this->size) {
                while (isset($black[$white])) $white++;
                $this->mapping[$b] = $white++;
            }
        }
    }

    function pick() {
        $index = $this->size > 0 ? mt_rand(0, $this->size - 1) : 0;
        return array_key_exists($index, $this->mapping) ? $this->mapping[$index] : $index;
    }
}
