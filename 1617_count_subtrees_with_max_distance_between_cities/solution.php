<?php
// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function countSubgraphsForEachDiameter($n, $edges) {
        $adj = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $a = $e[0] - 1;
            $b = $e[1] - 1;
            $adj[$a][] = $b;
            $adj[$b][] = $a;
        }
        $ans = array_fill(0, $n - 1, 0);
        $total = 1 << $n;
        for ($mask = 1; $mask < $total; $mask++) {
            if (($mask & ($mask - 1)) === 0) {
                continue;
            }
            $start = 0;
            $tmp = $mask;
            while (($tmp & 1) === 0) {
                $tmp >>= 1;
                $start++;
            }
            $bfs = function ($src) use ($mask, $adj) {
                $dist = [$src => 0];
                $q = [$src];
                for ($qi = 0; $qi < count($q); $qi++) {
                    $u = $q[$qi];
                    foreach ($adj[$u] as $v) {
                        if ((($mask >> $v) & 1) && !isset($dist[$v])) {
                            $dist[$v] = $dist[$u] + 1;
                            $q[] = $v;
                        }
                    }
                }
                $far = $src;
                foreach ($dist as $node => $d) {
                    if ($d > $dist[$far]) {
                        $far = $node;
                    }
                }
                return [$far, $dist];
            };
            [$far, $seen] = $bfs($start);
            $bits = 0;
            $tmp = $mask;
            while ($tmp) {
                $bits += $tmp & 1;
                $tmp >>= 1;
            }
            if (count($seen) === $bits) {
                [, $dist] = $bfs($far);
                $ans[max($dist) - 1]++;
            }
        }
        return $ans;
    }
}
