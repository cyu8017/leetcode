<?php
// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

class Solution {
    function join($arr1, $arr2) {
        $byId = [];
        foreach ($arr1 as $obj) $byId[$obj['id']] = $obj;
        foreach ($arr2 as $obj) {
            $id = $obj['id'];
            if (isset($byId[$id])) $byId[$id] = array_merge($byId[$id], $obj);
            else $byId[$id] = $obj;
        }
        $vals = array_values($byId);
        usort($vals, function($a, $b) { return $a['id'] <=> $b['id']; });
        return $vals;
    }
}
