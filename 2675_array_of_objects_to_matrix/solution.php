<?php
// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

class Solution {
    function jsonToMatrix($arr) {
        $isObj = function($x) {
            return is_array($x) && !array_is_list($x);
        };
        $flatten = function($obj, $prefix, &$out) use (&$flatten, $isObj) {
            if (!is_array($obj)) {
                $out[$prefix] = $obj;
                return;
            }
            if (array_is_list($obj)) {
                if (count($obj) === 0) return;
                for ($i = 0; $i < count($obj); $i++) {
                    $flatten($obj[$i], $prefix !== "" ? $prefix . "." . $i : (string)$i, $out);
                }
                return;
            }
            if (count($obj) === 0) return;
            foreach ($obj as $k => $v) {
                $flatten($v, $prefix !== "" ? $prefix . "." . $k : (string)$k, $out);
            }
        };
        $maps = [];
        foreach ($arr as $o) {
            $m = [];
            $flatten($o, "", $m);
            $maps[] = $m;
        }
        $keySet = [];
        foreach ($maps as $m) {
            foreach ($m as $k => $_) $keySet[$k] = true;
        }
        $keys = array_keys($keySet);
        sort($keys);
        $mat = [$keys];
        foreach ($maps as $m) {
            $row = [];
            foreach ($keys as $k) $row[] = array_key_exists($k, $m) ? $m[$k] : "";
            $mat[] = $row;
        }
        return $mat;
    }
}
