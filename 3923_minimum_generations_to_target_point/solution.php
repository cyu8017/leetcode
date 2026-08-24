<?php
// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

class Solution {
    function key($a, $b, $c) {
        return $a . ',' . $b . ',' . $c;
    }
    function minGenerations($points, $target) {
        $targetKey = $this->key($target[0], $target[1], $target[2]);
        $generation = [];
        $all = [];
        foreach ($points as $values) {
            $k = $this->key($values[0], $values[1], $values[2]);
            $generation[$k] = 0;
            $all[] = [$values[0], $values[1], $values[2]];
        }
        if (isset($generation[$targetKey])) return $generation[$targetKey];
        for ($current = 1; ; $current++) {
            $limit = count($all);
            $added = [];
            for ($i = 0; $i < $limit; $i++) {
                for ($j = $i + 1; $j < $limit; $j++) {
                    $pi = $all[$i];
                    $pj = $all[$j];
                    if ($pi[0] === $pj[0] && $pi[1] === $pj[1] && $pi[2] === $pj[2]) continue;
                    $p = [intdiv($pi[0] + $pj[0], 2), intdiv($pi[1] + $pj[1], 2), intdiv($pi[2] + $pj[2], 2)];
                    $k = $this->key($p[0], $p[1], $p[2]);
                    if (!isset($generation[$k])) {
                        $generation[$k] = $current;
                        $added[] = $p;
                    }
                }
            }
            if (isset($generation[$targetKey])) return $generation[$targetKey];
            if (count($added) === 0) return -1;
            foreach ($added as $p) $all[] = $p;
        }
    }
}
