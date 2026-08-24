<?php
// LeetCode 2618 - Check if Object Instance of Class
// https://leetcode.com/problems/check-if-object-instance-of-class/

class Solution {
    function checkIfInstanceOf($obj, $classFunction) {
        if ($obj === null) return false;
        if (is_object($classFunction)) {
            $classFunction = get_class($classFunction);
        }
        if (!is_string($classFunction) || $classFunction === '') return false;
        if (is_object($obj)) return $obj instanceof $classFunction;
        $map = [
            'integer' => ['int', 'integer'],
            'double' => ['float', 'double'],
            'string' => ['string'],
            'boolean' => ['bool', 'boolean'],
            'array' => ['array'],
        ];
        $t = gettype($obj);
        if (!isset($map[$t])) return false;
        return in_array(strtolower($classFunction), $map[$t], true);
    }
}
