<?php
// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

class Solution {
    function minMoves($classroom, $energy) {
        $m = count($classroom);
        $n = strlen($classroom[0]);
        $d = [];
        for ($i = 0; $i < $m; $i++) $d[$i] = array_fill(0, $n, 0);
        $x = 0;
        $y = 0;
        $cnt = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $c = $classroom[$i][$j];
                if ($c === 'S') { $x = $i; $y = $j; }
                else if ($c === 'L') $d[$i][$j] = $cnt++;
            }
        }
        if ($cnt === 0) return 0;
        $vis = [];
        for ($i = 0; $i < $m; $i++) {
            $vis[$i] = [];
            for ($j = 0; $j < $n; $j++) {
                $vis[$i][$j] = [];
                for ($e = 0; $e <= $energy; $e++)
                    $vis[$i][$j][$e] = array_fill(0, 1 << $cnt, false);
            }
        }
        $q = [[$x, $y, $energy, (1 << $cnt) - 1]];
        $vis[$x][$y][$energy][(1 << $cnt) - 1] = true;
        $dirs = [-1, 0, 1, 0, -1];
        $ans = 0;
        while (count($q)) {
            $t = $q;
            $q = [];
            foreach ($t as $s) {
                $i = $s[0];
                $j = $s[1];
                $curEnergy = $s[2];
                $mask = $s[3];
                if ($mask === 0) return $ans;
                if ($curEnergy <= 0) continue;
                for ($k = 0; $k < 4; $k++) {
                    $nx = $i + $dirs[$k];
                    $ny = $j + $dirs[$k + 1];
                    if ($nx >= 0 && $nx < $m && $ny >= 0 && $ny < $n && $classroom[$nx][$ny] !== 'X') {
                        $nxtEnergy = $classroom[$nx][$ny] === 'R' ? $energy : $curEnergy - 1;
                        $nxtMask = $mask;
                        if ($classroom[$nx][$ny] === 'L') $nxtMask &= ~(1 << $d[$nx][$ny]);
                        if (!$vis[$nx][$ny][$nxtEnergy][$nxtMask]) {
                            $vis[$nx][$ny][$nxtEnergy][$nxtMask] = true;
                            $q[] = [$nx, $ny, $nxtEnergy, $nxtMask];
                        }
                    }
                }
            }
            $ans++;
        }
        return -1;
    }
}
