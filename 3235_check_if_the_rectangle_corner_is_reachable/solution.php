<?php
// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

class Solution {
    private $circles;
    private $n;
    private $vis;
    private $xCorner;
    private $yCorner;

    function canReachCorner($xCorner, $yCorner, $circles) {
        $this->circles = $circles;
        $this->n = count($circles);
        $this->vis = array_fill(0, $this->n, false);
        $this->xCorner = $xCorner;
        $this->yCorner = $yCorner;
        for ($i = 0; $i < $this->n; $i++) {
            $x = $circles[$i][0];
            $y = $circles[$i][1];
            $r = $circles[$i][2];
            if ($this->inCircle(0, 0, $x, $y, $r) || $this->inCircle($xCorner, $yCorner, $x, $y, $r)) return false;
            if (!$this->vis[$i] && $this->crossLeftTop($x, $y, $r) && $this->dfs($i)) return false;
        }
        return true;
    }

    private function inCircle($x, $y, $cx, $cy, $r) {
        $dx = $x - $cx;
        $dy = $y - $cy;
        return $dx * $dx + $dy * $dy <= $r * $r;
    }

    private function crossLeftTop($cx, $cy, $r) {
        $a = abs($cx) <= $r && $cy >= 0 && $cy <= $this->yCorner;
        $b = abs($cy - $this->yCorner) <= $r && $cx >= 0 && $cx <= $this->xCorner;
        return $a || $b;
    }

    private function crossRightBottom($cx, $cy, $r) {
        $a = abs($cx - $this->xCorner) <= $r && $cy >= 0 && $cy <= $this->yCorner;
        $b = abs($cy) <= $r && $cx >= 0 && $cx <= $this->xCorner;
        return $a || $b;
    }

    private function dfs($i) {
        $x1 = $this->circles[$i][0];
        $y1 = $this->circles[$i][1];
        $r1 = $this->circles[$i][2];
        if ($this->crossRightBottom($x1, $y1, $r1)) return true;
        $this->vis[$i] = true;
        for ($j = 0; $j < $this->n; $j++) {
            if ($this->vis[$j]) continue;
            $x2 = $this->circles[$j][0];
            $y2 = $this->circles[$j][1];
            $r2 = $this->circles[$j][2];
            if (($x1 - $x2) * ($x1 - $x2) + ($y1 - $y2) * ($y1 - $y2) > ($r1 + $r2) * ($r1 + $r2)) continue;
            if ($x1 * $r2 + $x2 * $r1 < ($r1 + $r2) * $this->xCorner
                && $y1 * $r2 + $y2 * $r1 < ($r1 + $r2) * $this->yCorner
                && $this->dfs($j)) return true;
        }
        return false;
    }
}
