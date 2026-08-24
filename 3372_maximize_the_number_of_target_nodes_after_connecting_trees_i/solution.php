<?php
// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

class Solution {
    function buildTree($n, $edges) {
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        return $g;
    }

    function countWithin($g, $start, $k) {
        if ($k < 0) return 0;
        $n = count($g);
        $vis = array_fill(0, $n, false);
        $q = [[$start, 0]];
        $vis[$start] = true;
        $cnt = 0;
        $head = 0;
        while ($head < count($q)) {
            $cur = $q[$head++];
            $u = $cur[0];
            $d = $cur[1];
            $cnt++;
            if ($d === $k) continue;
            foreach ($g[$u] as $v) {
                if (!$vis[$v]) {
                    $vis[$v] = true;
                    $q[] = [$v, $d + 1];
                }
            }
        }
        return $cnt;
    }

    function maxTargetNodes($edges1, $edges2, $k) {
        $n = count($edges1) + 1;
        $m = count($edges2) + 1;
        $g1 = $this->buildTree($n, $edges1);
        $g2 = $this->buildTree($m, $edges2);
        $cnt1 = [];
        for ($i = 0; $i < $n; $i++) $cnt1[$i] = $this->countWithin($g1, $i, $k);
        $best2 = 0;
        if ($k > 0) {
            for ($i = 0; $i < $m; $i++) {
                $c = $this->countWithin($g2, $i, $k - 1);
                if ($c > $best2) $best2 = $c;
            }
        }
        $ans = [];
        for ($i = 0; $i < $n; $i++) $ans[$i] = $cnt1[$i] + $best2;
        return $ans;
    }
}
