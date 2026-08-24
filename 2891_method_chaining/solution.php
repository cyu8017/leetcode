<?php
// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/

class Solution {
    function findHeavyAnimals($animals) {
        $filtered = [];
        foreach ($animals as $r) {
            $w = (is_array($r) && isset($r[3]) && !isset($r['weight'])) ? $r[3] : $r['weight'];
            if ($w > 100) $filtered[] = $r;
        }
        usort($filtered, function($a, $b) {
            $wa = (is_array($a) && isset($a[3]) && !isset($a['weight'])) ? $a[3] : $a['weight'];
            $wb = (is_array($b) && isset($b[3]) && !isset($b['weight'])) ? $b[3] : $b['weight'];
            return $wb <=> $wa;
        });
        $out = [];
        foreach ($filtered as $r) {
            $name = (is_array($r) && isset($r[0]) && !isset($r['name'])) ? $r[0] : $r['name'];
            $out[] = ['name' => $name];
        }
        return $out;
    }
}
