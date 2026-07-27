<?php
// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution {
    function minimumJumps($forbidden, $a, $b, $x) {
        $bad = array_flip($forbidden);
        $limit = max(array_merge([$x], $forbidden)) + $a + $b;
        $q = [[0, 0, false]];
        $seen = ["0_0" => true];
        $qi = 0;
        while ($qi < count($q)) {
            [$p, $d, $back] = $q[$qi++];
            if ($p === $x) return $d;
            $cands = [[$p + $a, false], [$p - $b, true]];
            foreach ($cands as [$np, $nb]) {
                if ($np < 0 || $np > $limit) continue;
                if (isset($bad[$np])) continue;
                if ($back && $nb) continue;
                $key = $np . "_" . ($nb ? "1" : "0");
                if (isset($seen[$key])) continue;
                $seen[$key] = true;
                $q[] = [$np, $d + 1, $nb];
            }
        }
        return -1;
    }
}
