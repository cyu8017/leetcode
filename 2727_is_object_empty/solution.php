<?php
// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/

class Solution {
    function isEmpty($obj) {
        if (is_array($obj)) return count($obj) === 0;
        if (is_object($obj)) return count(get_object_vars($obj)) === 0;
        return empty($obj);
    }
}
