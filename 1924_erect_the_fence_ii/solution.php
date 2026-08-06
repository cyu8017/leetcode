<?php
// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

class Solution {
    /**
     * @param Integer[][] $trees
     * @return Float[]
     */
    function outerTrees($trees) {
        $pts = $trees;
        shuffle($pts);

        $circle = null;
        $n = count($pts);
        for ($i = 0; $i < $n; $i++) {
            $p = $pts[$i];
            if ($circle === null || !$this->inside($circle, $p)) {
                $circle = [$p, 0.0];
                for ($j = 0; $j < $i; $j++) {
                    $q = $pts[$j];
                    if (!$this->inside($circle, $q)) {
                        $circle = $this->circle2($p, $q);
                        for ($k = 0; $k < $j; $k++) {
                            $r = $pts[$k];
                            if (!$this->inside($circle, $r)) {
                                $circle = $this->circle3($p, $q, $r);
                            }
                        }
                    }
                }
            }
        }

        return [$circle[0][0], $circle[0][1], $circle[1]];
    }

    private function dist($a, $b) {
        $dx = $a[0] - $b[0];
        $dy = $a[1] - $b[1];
        return sqrt($dx * $dx + $dy * $dy);
    }

    private function circle2($a, $b) {
        $c = [($a[0] + $b[0]) / 2.0, ($a[1] + $b[1]) / 2.0];
        return [$c, $this->dist($a, $b) / 2.0];
    }

    private function circle3($a, $b, $c) {
        $ax = $a[0];
        $ay = $a[1];
        $bx = $b[0];
        $by = $b[1];
        $cx = $c[0];
        $cy = $c[1];
        $d = 2 * ($ax * ($by - $cy) + $bx * ($cy - $ay) + $cx * ($ay - $by));
        if (abs($d) < 1e-12) {
            $candidates = [
                $this->circle2($a, $b),
                $this->circle2($a, $c),
                $this->circle2($b, $c),
            ];
            usort($candidates, function ($x, $y) {
                return $x[1] <=> $y[1];
            });
            return $candidates[0];
        }
        $ux = (($ax * $ax + $ay * $ay) * ($by - $cy)
            + ($bx * $bx + $by * $by) * ($cy - $ay)
            + ($cx * $cx + $cy * $cy) * ($ay - $by)) / $d;
        $uy = (($ax * $ax + $ay * $ay) * ($cx - $bx)
            + ($bx * $bx + $by * $by) * ($ax - $cx)
            + ($cx * $cx + $cy * $cy) * ($bx - $ax)) / $d;
        $center = [$ux, $uy];
        return [$center, $this->dist($center, $a)];
    }

    private function inside($cir, $p) {
        return $this->dist($cir[0], $p) <= $cir[1] + 1e-9;
    }
}
