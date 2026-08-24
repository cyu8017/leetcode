<?php
// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

class MapSum {
    private $values = [];
    private $prefixSums = [];

    function __construct() {}

    function insert($key, $val) {
        $delta = $val - ($this->values[$key] ?? 0);
        $this->values[$key] = $val;
        for ($i = 1; $i <= strlen($key); ++$i) {
            $prefix = substr($key, 0, $i);
            $this->prefixSums[$prefix] = ($this->prefixSums[$prefix] ?? 0) + $delta;
        }
    }

    function sum($prefix) {
        return $this->prefixSums[$prefix] ?? 0;
    }
}
