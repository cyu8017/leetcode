<?php
// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

class Solution {
    function floodFill($image, $sr, $sc, $color) {
        $original = $image[$sr][$sc];
        if ($original === $color) return $image;
        $dfs = function ($r, $c) use (&$dfs, &$image, $original, $color) {
            if ($r < 0 || $r >= count($image) || $c < 0 || $c >= count($image[0]) || $image[$r][$c] !== $original) return;
            $image[$r][$c] = $color;
            $dfs($r + 1, $c);
            $dfs($r - 1, $c);
            $dfs($r, $c + 1);
            $dfs($r, $c - 1);
        };
        $dfs($sr, $sc);
        return $image;
    }
}
