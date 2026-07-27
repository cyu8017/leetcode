<?php
// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

class Solution {
    private $memo = [];

    function getMaxGridHappiness($m, $n, $introvertsCount, $extrovertsCount) {
        $states = (int)pow(3, $n);
        $cells = [];
        $intro = [];
        $extro = [];
        $row = [];
        for ($s = 0; $s < $states; $s++) {
            $x = $s;
            $a = [];
            for ($j = 0; $j < $n; $j++) {
                $a[] = $x % 3;
                $x = intdiv($x, 3);
            }
            $cells[] = $a;
            $ic = 0;
            $ec = 0;
            $val = 0;
            for ($j = 0; $j < $n; $j++) {
                if ($a[$j] === 1) { $ic++; $val += 120; }
                elseif ($a[$j] === 2) { $ec++; $val += 40; }
            }
            $intro[] = $ic;
            $extro[] = $ec;
            for ($j = 1; $j < $n; $j++) {
                $val += $this->pair($a[$j - 1], $a[$j]);
            }
            $row[] = $val;
        }
        $compat = [];
        for ($a = 0; $a < $states; $a++) {
            $compat[$a] = [];
            for ($b = 0; $b < $states; $b++) {
                $sum = 0;
                for ($j = 0; $j < $n; $j++) {
                    $sum += $this->pair($cells[$a][$j], $cells[$b][$j]);
                }
                $compat[$a][$b] = $sum;
            }
        }
        $this->memo = [];
        return $this->dp(0, 0, $introvertsCount, $extrovertsCount, $m, $states, $row, $compat, $intro, $extro);
    }

    private function dp($r, $prev, $i, $e, $m, $states, $row, $compat, $intro, $extro) {
        if ($r === $m) return 0;
        $key = "$r,$prev,$i,$e";
        if (isset($this->memo[$key])) return $this->memo[$key];
        $best = 0;
        for ($s = 0; $s < $states; $s++) {
            if ($intro[$s] <= $i && $extro[$s] <= $e) {
                $best = max($best, $row[$s] + $compat[$prev][$s] + $this->dp($r + 1, $s, $i - $intro[$s], $e - $extro[$s], $m, $states, $row, $compat, $intro, $extro));
            }
        }
        return $this->memo[$key] = $best;
    }

    private function pair($a, $b) {
        if (!$a || !$b) return 0;
        return ($a === 1 ? -30 : 20) + ($b === 1 ? -30 : 20);
    }
}
