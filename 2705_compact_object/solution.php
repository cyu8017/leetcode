<?php
// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

class Solution {
    function compactObject($obj) {
        $truthy = function($v) {
            if (is_array($v)) return true;
            return (bool)$v;
        };
        if (is_array($obj) && array_is_list($obj)) {
            $out = [];
            foreach ($obj as $x) {
                $v = $this->compactObject($x);
                if ($truthy($v)) $out[] = $v;
            }
            return $out;
        }
        if (is_array($obj)) {
            $out = [];
            foreach ($obj as $k => $val) {
                $v = $this->compactObject($val);
                if ($truthy($v)) $out[$k] = $v;
            }
            return $out;
        }
        return $obj;
    }
}
