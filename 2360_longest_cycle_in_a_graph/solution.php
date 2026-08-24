<?php
// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution {
    function longestCycle($edges) {
        $n = count($edges);
        $vis = array_fill(0, $n, false);
        $ans = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($vis[$i]) continue;
            $dist = [];
            $cur = $i;
            $step = 0;
            while ($cur !== -1 && !$vis[$cur]) {
                $vis[$cur] = true;
                $dist[$cur] = $step;
                $cur = $edges[$cur];
                $step++;
            }
            if ($cur !== -1 && isset($dist[$cur])) {
                $ans = max($ans, $step - $dist[$cur]);
            }
        }
        return $ans;
    }
}
