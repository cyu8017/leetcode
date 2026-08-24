<?php
// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/

class Solution {
    function jsonStringify($object) {
        if ($object === null) return "null";
        if (is_string($object)) return '"' . $object . '"';
        if (is_int($object) || is_float($object) || is_bool($object)) {
            if (is_bool($object)) return $object ? "true" : "false";
            return (string)$object;
        }
        if (is_array($object) && array_is_list($object)) {
            $parts = [];
            foreach ($object as $x) $parts[] = $this->jsonStringify($x);
            return "[" . implode(",", $parts) . "]";
        }
        $parts = [];
        foreach ($object as $k => $v) {
            $parts[] = '"' . $k . '":' . $this->jsonStringify($v);
        }
        return "{" . implode(",", $parts) . "}";
    }
}
