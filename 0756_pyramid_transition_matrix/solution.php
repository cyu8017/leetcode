<?php
// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

class Solution {
    function pyramidTransition($bottom, $allowed) {
        $transitions = [];
        $memo = [];
        foreach ($allowed as $triple) {
            $key = substr($triple, 0, 2);
            if (!isset($transitions[$key])) $transitions[$key] = [];
            $transitions[$key][] = $triple[2];
        }
        $dfs = null;
        $build = function ($index, $options, $path) use (&$build, &$dfs) {
            if ($index === count($options)) return $dfs($path);
            foreach ($options[$index] as $ch) {
                if ($build($index + 1, $options, $path . $ch)) return true;
            }
            return false;
        };
        $dfs = function ($row) use (&$dfs, &$build, &$transitions, &$memo) {
            if (strlen($row) === 1) return true;
            if (array_key_exists($row, $memo)) return $memo[$row];
            $options = [];
            $rlen = strlen($row);
            for ($i = 0; $i + 1 < $rlen; $i++) {
                $key = substr($row, $i, 2);
                if (!isset($transitions[$key])) {
                    $memo[$row] = false;
                    return false;
                }
                $options[] = $transitions[$key];
            }
            $ok = $build(0, $options, '');
            $memo[$row] = $ok;
            return $ok;
        };
        return $dfs($bottom);
    }
}
