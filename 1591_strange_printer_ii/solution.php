<?php

class Solution {
    /**
     * @param Integer[][] $targetGrid
     * @return Boolean
     */
    function isPrintable($targetGrid) {
        $colors = [];
        $m = count($targetGrid);
        $n = count($targetGrid[0]);
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $colors[$targetGrid[$r][$c]] = true;
            }
        }
        $bounds = [];
        foreach ($colors as $color => $_) {
            $bounds[$color] = [PHP_INT_MAX, PHP_INT_MAX, -1, -1];
        }
        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $col = $targetGrid[$r][$c];
                $b = &$bounds[$col];
                $b[0] = min($b[0], $r);
                $b[1] = min($b[1], $c);
                $b[2] = max($b[2], $r);
                $b[3] = max($b[3], $c);
                unset($b);
            }
        }
        $graph = [];
        $indegree = [];
        foreach ($colors as $color => $_) {
            $graph[$color] = [];
            $indegree[$color] = 0;
        }
        foreach ($bounds as $color => $b) {
            for ($r = $b[0]; $r <= $b[2]; $r++) {
                for ($c = $b[1]; $c <= $b[3]; $c++) {
                    $other = $targetGrid[$r][$c];
                    if ($other !== $color && !isset($graph[$color][$other])) {
                        $graph[$color][$other] = true;
                        $indegree[$other]++;
                    }
                }
            }
        }
        $queue = [];
        foreach ($colors as $color => $_) {
            if ($indegree[$color] === 0) {
                $queue[] = $color;
            }
        }
        $seen = 0;
        while (!empty($queue)) {
            $color = array_shift($queue);
            $seen++;
            foreach ($graph[$color] as $nxt => $_) {
                $indegree[$nxt]--;
                if ($indegree[$nxt] === 0) {
                    $queue[] = $nxt;
                }
            }
        }
        return $seen === count($colors);
    }
}
