<?php
// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

class Solution {
    function maximumScore($scores, $edges) {
        $n = count($scores);
        $top = array_fill(0, $n, []);
        $g = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $g[$e[0]][] = $e[1];
            $g[$e[1]][] = $e[0];
        }
        for ($i = 0; $i < $n; $i++) {
            foreach ($g[$i] as $v) {
                $top[$i][] = $v;
                for ($j = count($top[$i]) - 1; $j > 0; $j--) {
                    if ($scores[$top[$i][$j]] > $scores[$top[$i][$j - 1]]) {
                        $tmp = $top[$i][$j];
                        $top[$i][$j] = $top[$i][$j - 1];
                        $top[$i][$j - 1] = $tmp;
                    }
                }
                if (count($top[$i]) > 3) $top[$i] = array_slice($top[$i], 0, 3);
            }
        }
        $ans = -1;
        foreach ($edges as $e) {
            $a = $e[0];
            $b = $e[1];
            foreach ($top[$a] as $c) {
                if ($c === $b) continue;
                foreach ($top[$b] as $d) {
                    if ($d === $a || $d === $c) continue;
                    $ans = max($ans, $scores[$a] + $scores[$b] + $scores[$c] + $scores[$d]);
                }
            }
        }
        return $ans;
    }
}
