<?php
// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

class Solution {
    /**
     * @param String[] $pieces
     * @param Integer[][] $positions
     * @return Integer
     */
    function countCombinations($pieces, $positions) {
        $dirs = [
            'rook' => [[1, 0], [-1, 0], [0, 1], [0, -1]],
            'bishop' => [[1, 1], [1, -1], [-1, 1], [-1, -1]],
            'queen' => [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]],
        ];
        $n = count($pieces);
        $allMoves = array_fill(0, $n, []);
        for ($i = 0; $i < $n; $i++) {
            $ms = [['dr' => 0, 'dc' => 0, 'steps' => 0]];
            $r = $positions[$i][0];
            $c = $positions[$i][1];
            foreach ($dirs[$pieces[$i]] as $d) {
                $nr = $r + $d[0];
                $nc = $c + $d[1];
                $step = 1;
                while ($nr >= 1 && $nr <= 8 && $nc >= 1 && $nc <= 8) {
                    $ms[] = ['dr' => $d[0], 'dc' => $d[1], 'steps' => $step];
                    $nr += $d[0];
                    $nc += $d[1];
                    $step++;
                }
            }
            $allMoves[$i] = $ms;
        }
        $chosen = array_fill(0, $n, null);
        $ans = 0;
        $okCombo = function ($end) use (&$chosen, $positions) {
            $maxT = 0;
            for ($i = 0; $i <= $end; $i++) $maxT = max($maxT, $chosen[$i]['steps']);
            for ($t = 1; $t <= $maxT; $t++) {
                $seen = [];
                for ($i = 0; $i <= $end; $i++) {
                    $m = $chosen[$i];
                    if ($m['steps'] === 0) { $pr = $positions[$i][0]; $pc = $positions[$i][1]; }
                    else {
                        $use = min($t, $m['steps']);
                        $pr = $positions[$i][0] + $m['dr'] * $use;
                        $pc = $positions[$i][1] + $m['dc'] * $use;
                    }
                    $key = $pr . "," . $pc;
                    if (isset($seen[$key])) return false;
                    $seen[$key] = true;
                }
            }
            return true;
        };
        $dfs = null;
        $dfs = function ($i) use (&$dfs, &$ans, &$chosen, &$allMoves, $pieces, $okCombo) {
            if ($i === count($pieces)) { $ans++; return; }
            foreach ($allMoves[$i] as $m) {
                $chosen[$i] = $m;
                if ($okCombo($i)) $dfs($i + 1);
            }
        };
        $dfs(0);
        return $ans;
    }
}
