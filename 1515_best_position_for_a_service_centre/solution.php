<?php
// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

class Solution {
    /**
     * @param Float[][] $positions
     * @return Float
     */
    function getMinDistSum($positions) {
        $n = count($positions);
        $x = 0.0;
        $y = 0.0;
        foreach ($positions as $p) {
            $x += $p[0];
            $y += $p[1];
        }
        $x /= $n;
        $y /= $n;

        for ($iter = 0; $iter < 10000; $iter++) {
            $numeratorX = 0.0;
            $numeratorY = 0.0;
            $denominator = 0.0;
            $coincident = null;
            foreach ($positions as $p) {
                $dx = $x - $p[0];
                $dy = $y - $p[1];
                $d = sqrt($dx * $dx + $dy * $dy);
                if ($d < 1e-12) {
                    $coincident = $p;
                    break;
                }
                $numeratorX += $p[0] / $d;
                $numeratorY += $p[1] / $d;
                $denominator += 1.0 / $d;
            }
            if ($coincident !== null) {
                $nx = $coincident[0];
                $ny = $coincident[1];
            } else {
                $nx = $numeratorX / $denominator;
                $ny = $numeratorY / $denominator;
            }
            $move = sqrt(($nx - $x) * ($nx - $x) + ($ny - $y) * ($ny - $y));
            $x = $nx;
            $y = $ny;
            if ($move < 1e-8) {
                break;
            }
        }

        $sum = 0.0;
        foreach ($positions as $p) {
            $dx = $x - $p[0];
            $dy = $y - $p[1];
            $sum += sqrt($dx * $dx + $dy * $dy);
        }
        return $sum;
    }
}
