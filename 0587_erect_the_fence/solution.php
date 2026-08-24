<?php
// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

class Solution {
    function outerTrees($trees) {
        $points = $trees;
        usort($points, function($a, $b) {
            return $a[0] !== $b[0] ? $a[0] <=> $b[0] : $a[1] <=> $b[1];
        });
        if (count($points) <= 1) return $points;
        $cross = function($o, $a, $b) {
            return ($a[0] - $o[0]) * ($b[1] - $o[1]) - ($a[1] - $o[1]) * ($b[0] - $o[0]);
        };
        $build = function($ordered) use ($cross) {
            $hull = [];
            foreach ($ordered as $point) {
                while (count($hull) >= 2 && $cross($hull[count($hull) - 2], $hull[count($hull) - 1], $point) < 0) {
                    array_pop($hull);
                }
                $hull[] = $point;
            }
            return $hull;
        };
        $lower = $build($points);
        $rev = array_reverse($points);
        $upper = $build($rev);
        $seen = [];
        $unique = [];
        $addUnique = function($point) use (&$seen, &$unique) {
            $key = $point[0] . "," . $point[1];
            if (!isset($seen[$key])) {
                $seen[$key] = true;
                $unique[] = $point;
            }
        };
        for ($i = 0; $i + 1 < count($lower); ++$i) $addUnique($lower[$i]);
        for ($i = 0; $i + 1 < count($upper); ++$i) $addUnique($upper[$i]);
        return $unique;
    }
}
