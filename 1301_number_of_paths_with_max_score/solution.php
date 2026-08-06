<?php
class Solution {
    function pathsWithMaxScore($board) {
        $mod = 1000000007;
        $n = count($board);
        $score = array_fill(0, $n, array_fill(0, $n, -1));
        $ways = array_fill(0, $n, array_fill(0, $n, 0));
        $score[$n - 1][$n - 1] = 0;
        $ways[$n - 1][$n - 1] = 1;
        for ($r = $n - 1; $r >= 0; $r--) {
            for ($c = $n - 1; $c >= 0; $c--) {
                if ($board[$r][$c] === "X" || ($r === $n - 1 && $c === $n - 1)) continue;
                $best = -1;
                $count = 0;
                foreach ([[$r + 1, $c], [$r, $c + 1], [$r + 1, $c + 1]] as [$nr, $nc]) {
                    if ($nr < $n && $nc < $n && $score[$nr][$nc] >= 0) {
                        if ($score[$nr][$nc] > $best) {
                            $best = $score[$nr][$nc];
                            $count = $ways[$nr][$nc];
                        } elseif ($score[$nr][$nc] === $best) {
                            $count = ($count + $ways[$nr][$nc]) % $mod;
                        }
                    }
                }
                if ($best >= 0) {
                    $ch = $board[$r][$c];
                    $score[$r][$c] = $best + (ctype_digit($ch) ? intval($ch) : 0);
                    $ways[$r][$c] = $count;
                }
            }
        }
        return [max($score[0][0], 0), $ways[0][0]];
    }
}
