<?php
// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

class ImmutableHelper {
    private $obj;

    function __construct($obj) {
        $this->obj = $obj;
    }

    function produce($mutator) {
        $copy = unserialize(serialize($this->obj));
        $mutator($copy);
        return $copy;
    }
}

class Solution {
    function ImmutableHelper($obj, $mutators = null) {
        return new ImmutableHelper($obj);
    }
}
