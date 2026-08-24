<?php
// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

class Solution {
    function numberOfComponents($properties, $k) {
        $n = count($properties);
        $sets = [];
        for ($i = 0; $i < $n; $i++) {
            $sets[$i] = [];
            foreach ($properties[$i] as $v) $sets[$i][$v] = true;
        }
        $parent = [];
        for ($i = 0; $i < $n; $i++) $parent[$i] = $i;
        $find = null;
        $find = function($x) use (&$find, &$parent) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $unite = function($a, $b) use ($find, &$parent) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra !== $rb) $parent[$ra] = $rb;
        };
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $cnt = 0;
                foreach ($sets[$i] as $v => $_) if (isset($sets[$j][$v])) $cnt++;
                if ($cnt >= $k) $unite($i, $j);
            }
        }
        $comp = [];
        for ($i = 0; $i < $n; $i++) $comp[$find($i)] = true;
        return count($comp);
    }
}
