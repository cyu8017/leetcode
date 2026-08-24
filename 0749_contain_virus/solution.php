<?php
// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

class Solution {
    function containVirus($isInfected) {
        $m = count($isInfected);
        $n = count($isInfected[0]);
        $walls = 0;
        $pack = function ($r, $c) { return $r * 1000000 + $c; };
        $unpack = function ($key) { return [intdiv($key, 1000000), $key % 1000000]; };
        while (true) {
            $seen = [];
            $regions = [];
            $frontiers = [];
            $perimeters = [];
            for ($i = 0; $i < $m; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    $key = $pack($i, $j);
                    if ($isInfected[$i][$j] === 1 && !isset($seen[$key])) {
                        $stack = [[$i, $j]];
                        $seen[$key] = true;
                        $region = [];
                        $frontier = [];
                        $perimeter = 0;
                        $dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
                        while (count($stack) > 0) {
                            $cell = array_pop($stack);
                            $r = $cell[0];
                            $c = $cell[1];
                            $region[$pack($r, $c)] = true;
                            foreach ($dirs as $d) {
                                $nr = $r + $d[0];
                                $nc = $c + $d[1];
                                if ($nr < 0 || $nr >= $m || $nc < 0 || $nc >= $n) continue;
                                $nk = $pack($nr, $nc);
                                if ($isInfected[$nr][$nc] === 1) {
                                    if (!isset($seen[$nk])) {
                                        $seen[$nk] = true;
                                        $stack[] = [$nr, $nc];
                                    }
                                } else if ($isInfected[$nr][$nc] === 0) {
                                    $frontier[$nk] = true;
                                    $perimeter++;
                                }
                            }
                        }
                        $regions[] = $region;
                        $frontiers[] = $frontier;
                        $perimeters[] = $perimeter;
                    }
                }
            }
            if (count($regions) === 0) break;
            $quarantine = 0;
            for ($i = 1; $i < count($regions); $i++)
                if (count($frontiers[$i]) > count($frontiers[$quarantine])) $quarantine = $i;
            if (count($frontiers[$quarantine]) === 0) break;
            $walls += $perimeters[$quarantine];
            foreach ($regions[$quarantine] as $cell => $_) {
                [$r, $c] = $unpack($cell);
                $isInfected[$r][$c] = -1;
            }
            for ($index = 0; $index < count($frontiers); $index++) {
                if ($index === $quarantine) continue;
                foreach ($frontiers[$index] as $cell => $_) {
                    [$r, $c] = $unpack($cell);
                    $isInfected[$r][$c] = 1;
                }
            }
        }
        return $walls;
    }
}
