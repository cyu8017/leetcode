<?php
// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

class MyHashMap {
    private $data = [];

    function __construct() {
        $this->data = [];
    }

    function put($key, $value) {
        $this->data[$key] = $value;
    }

    function get($key) {
        return array_key_exists($key, $this->data) ? $this->data[$key] : -1;
    }

    function remove($key) {
        unset($this->data[$key]);
    }
}
