<?php
// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

class AutocompleteSystem {
    private $counts = [];
    private $current = "";

    function __construct($sentences, $times) {
        for ($i = 0; $i < count($sentences); ++$i) {
            $this->counts[$sentences[$i]] = ($this->counts[$sentences[$i]] ?? 0) + $times[$i];
        }
    }

    function input($c) {
        if ($c === "#") {
            $sentence = $this->current;
            $this->counts[$sentence] = ($this->counts[$sentence] ?? 0) + 1;
            $this->current = "";
            return [];
        }
        $this->current .= $c;
        $prefix = $this->current;
        $matches = [];
        foreach ($this->counts as $sentence => $_) {
            if (strncmp($sentence, $prefix, strlen($prefix)) === 0) $matches[] = $sentence;
        }
        usort($matches, function($a, $b) {
            $ca = $this->counts[$a];
            $cb = $this->counts[$b];
            if ($ca !== $cb) return $cb <=> $ca;
            return $a <=> $b;
        });
        return count($matches) > 3 ? array_slice($matches, 0, 3) : $matches;
    }
}
