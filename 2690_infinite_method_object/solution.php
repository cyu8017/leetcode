<?php
// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/

class InfiniteObject {
    function __call($name, $args) {
        return "Hello World";
    }
}

class Solution {
    function createInfiniteObject($method = null) {
        return new InfiniteObject();
    }
}
