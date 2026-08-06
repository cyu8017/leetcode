<?php
class Solution {
    function findCriticalAndPseudoCriticalEdges($n, $edges) {
        $es = [];
        foreach ($edges as $i => [$a, $b, $w]) $es[] = [$w, $a, $b, $i];
        usort($es, function($x, $y) { return $x[0] <=> $y[0]; });
        $mst = function($skip = -1, $force = -1) use ($n, $es) {
            $parent = range(0, $n - 1);
            $find = function($x) use (&$parent, &$find) {
                while ($x !== $parent[$x]) {
                    $parent[$x] = $parent[$parent[$x]];
                    $x = $parent[$x];
                }
                return $x;
            };
            $total = 0;
            $used = 0;
            if ($force >= 0) {
                [$w, $a, $b] = $es[$force];
                $parent[$find($a)] = $find($b);
                $total += $w;
                $used++;
            }
            foreach ($es as $j => [$w, $a, $b]) {
                if ($j === $skip || $j === $force) continue;
                $x = $find($a);
                $y = $find($b);
                if ($x !== $y) {
                    $parent[$x] = $y;
                    $total += $w;
                    $used++;
                }
            }
            return $used === $n - 1 ? $total : PHP_INT_MAX;
        };
        $base = $mst();
        $critical = [];
        $pseudo = [];
        foreach ($es as $j => $edge) {
            if ($mst($j) > $base) $critical[] = $edge[3];
            elseif ($mst(-1, $j) === $base) $pseudo[] = $edge[3];
        }
        sort($critical);
        sort($pseudo);
        return [$critical, $pseudo];
    }
}
