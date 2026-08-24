<?php
// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution {
    function colorTheArray($n, $queries) {
        $colors = array_fill(0, $n, 0);
        $ans = array_fill(0, count($queries), 0);
        $same = 0;
        for ($i = 0; $i < count($queries); $i++) {
            $idx = $queries[$i][0];
            $color = $queries[$i][1];
            if ($colors[$idx] !== 0) {
                if ($idx > 0 && $colors[$idx] === $colors[$idx - 1]) $same--;
                if ($idx + 1 < $n && $colors[$idx] === $colors[$idx + 1]) $same--;
            }
            $colors[$idx] = $color;
            if ($idx > 0 && $colors[$idx] === $colors[$idx - 1]) $same++;
            if ($idx + 1 < $n && $colors[$idx] === $colors[$idx + 1]) $same++;
            $ans[$i] = $same;
        }
        return $ans;
    }
}
