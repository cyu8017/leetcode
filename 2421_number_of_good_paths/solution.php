<?php
// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

class Solution {
    function numberOfGoodPaths($vals, $edges) {
        $n = count($vals);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $parent = range(0, $n - 1);
        $size = array_fill(0, $n, 1);
        $find = function ($x) use (&$find, &$parent) {
            if ($parent[$x] !== $x) $parent[$x] = $find($parent[$x]);
            return $parent[$x];
        };
        $nodes = range(0, $n - 1);
        usort($nodes, function ($a, $b) use ($vals) {
            return $vals[$a] <=> $vals[$b];
        });
        $ans = $n;
        for ($i = 0; $i < $n; ) {
            $j = $i;
            while ($j < $n && $vals[$nodes[$j]] === $vals[$nodes[$i]]) $j++;
            for ($k = $i; $k < $j; $k++) {
                $u = $nodes[$k];
                foreach ($g[$u] as $v) {
                    if ($vals[$v] <= $vals[$u]) {
                        $ru = $find($u);
                        $rv = $find($v);
                        if ($ru !== $rv) {
                            $parent[$ru] = $rv;
                            $size[$rv] += $size[$ru];
                        }
                    }
                }
            }
            $freq = [];
            for ($k = $i; $k < $j; $k++) {
                $r = $find($nodes[$k]);
                if (!isset($freq[$r])) $freq[$r] = 0;
                $freq[$r]++;
            }
            foreach ($freq as $c) $ans += intdiv($c * ($c - 1), 2);
            $i = $j;
        }
        return $ans;
    }
}
