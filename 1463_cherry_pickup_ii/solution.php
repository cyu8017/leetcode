<?php
class Solution {
    function cherryPickup($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $dp = ["0," . ($n - 1) => $grid[0][0] + ($n > 1 ? $grid[0][$n - 1] : 0)];
        for ($r = 1; $r < $m; $r++) {
            $nxt = [];
            foreach ($dp as $key => $score) {
                [$a, $b] = array_map('intval', explode(",", $key));
                for ($na = $a - 1; $na <= $a + 1; $na++) {
                    for ($nb = $b - 1; $nb <= $b + 1; $nb++) {
                        if ($na >= 0 && $na < $n && $nb >= 0 && $nb < $n) {
                            $val = $score + $grid[$r][$na] + ($na !== $nb ? $grid[$r][$nb] : 0);
                            $nk = "$na,$nb";
                            $nxt[$nk] = max($nxt[$nk] ?? -1, $val);
                        }
                    }
                }
            }
            $dp = $nxt;
        }
        return max($dp);
    }
}
