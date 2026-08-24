<?php
// LeetCode 3898 - Find the Degree of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/

class Solution {
    function findDegrees($matrix) {
        $ans = array_fill(0, count($matrix), 0);
        $n = count($matrix);
        for ($i = 0; $i < $n; $i++) {
            foreach ($matrix[$i] as $x) $ans[$i] += $x;
        }
        return $ans;
    }
}
