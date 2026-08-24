<?php
// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution {
    /**
     * @param Integer[][] $bombs
     * @return Integer
     */
    function maximumDetonation($bombs) {
        $n = count($bombs);
        $g = array_fill(0, $n, []);
        for ($i = 0; $i < $n; $i++) {
            $x1 = $bombs[$i][0];
            $y1 = $bombs[$i][1];
            $r1 = $bombs[$i][2];
            for ($j = 0; $j < $n; $j++) {
                if ($i === $j) continue;
                $dx = $bombs[$j][0] - $x1;
                $dy = $bombs[$j][1] - $y1;
                if ($dx * $dx + $dy * $dy <= $r1 * $r1) $g[$i][] = $j;
            }
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $vis = array_fill(0, $n, false);
            $q = [$i];
            $vis[$i] = true;
            $cnt = 0;
            while ($q) {
                $u = array_shift($q);
                $cnt++;
                foreach ($g[$u] as $v) {
                    if (!$vis[$v]) {
                        $vis[$v] = true;
                        $q[] = $v;
                    }
                }
            }
            $ans = max($ans, $cnt);
        }
        return $ans;
    }
}
