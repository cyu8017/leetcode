<?php
// LeetCode 3787 - Find Diameter Endpoints of a Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

class Solution {
    function findSpecialNodes($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        $bfs = function($start) use ($n, $g) {
            $dist = array_fill(0, $n, -1);
            $dist[$start] = 0;
            $q = [$start];
            $far = $start;
            for ($head = 0; $head < count($q); $head++) {
                $u = $q[$head];
                if ($dist[$u] > $dist[$far]) $far = $u;
                foreach ($g[$u] as $v) {
                    if ($dist[$v] === -1) {
                        $dist[$v] = $dist[$u] + 1;
                        $q[] = $v;
                    }
                }
            }
            return [$far, $dist];
        };
        $tmp = $bfs(0);
        $a = $tmp[0];
        $tmp = $bfs($a);
        $b = $tmp[0];
        $dist1 = $tmp[1];
        $tmp = $bfs($b);
        $dist2 = $tmp[1];
        $d = $dist1[$b];
        $ans = array_fill(0, $n, '0');
        for ($i = 0; $i < $n; $i++) {
            if ($dist1[$i] === $d || $dist2[$i] === $d) $ans[$i] = '1';
        }
        return implode('', $ans);
    }
}
