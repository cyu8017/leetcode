<?php
// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

class MyHashSet {
    private $data = [];

    function __construct() {
        $this->data = [];
    }

    function add($key) {
        $this->data[$key] = true;
    }

    function remove($key) {
        unset($this->data[$key]);
    }

    function contains($key) {
        return isset($this->data[$key]);
    }
}
