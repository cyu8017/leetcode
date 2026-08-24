<?php
// LeetCode 2723 - Add Two Promises
// https://leetcode.com/problems/add-two-promises/

class Solution {
    function addTwoPromises($promise1, $promise2) {
        $a = is_callable($promise1) ? $promise1() : $promise1;
        $b = is_callable($promise2) ? $promise2() : $promise2;
        return $a + $b;
    }
}
