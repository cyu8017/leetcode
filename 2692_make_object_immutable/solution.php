<?php
// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

class ImmutableArray {
    private $data;
    function __construct($data) { $this->data = $data; }
    function __get($prop) {
        if (in_array($prop, ["pop", "push", "shift", "unshift", "splice", "sort", "reverse"], true)) {
            throw new Exception("Error Calling Method: " . $prop);
        }
        $v = $this->data[$prop] ?? null;
        if (is_array($v)) return (new Solution())->makeImmutable($v);
        return $v;
    }
    function __set($prop, $value) {
        throw new Exception("Error Modifying Index: " . $prop);
    }
}

class ImmutableObject {
    private $data;
    function __construct($data) { $this->data = $data; }
    function __get($prop) {
        $v = $this->data[$prop] ?? null;
        if (is_array($v)) return (new Solution())->makeImmutable($v);
        return $v;
    }
    function __set($prop, $value) {
        throw new Exception("Error Modifying: " . $prop);
    }
}

class Solution {
    function makeImmutable($obj) {
        if ($obj === null || !is_array($obj)) return $obj;
        if (array_is_list($obj)) return new ImmutableArray($obj);
        return new ImmutableObject($obj);
    }
}
