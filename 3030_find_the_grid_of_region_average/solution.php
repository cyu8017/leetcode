<?php
// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

class Solution {
    function resultGrid($image, $threshold) {
        $n = count($image);
        $m = count($image[0]);
        $ans = [];
        $ct = [];
        for ($i = 0; $i < $n; $i++) {
            $ans[$i] = array_fill(0, $m, 0);
            $ct[$i] = array_fill(0, $m, 0);
        }
        for ($i = 0; $i + 2 < $n; $i++) {
            for ($j = 0; $j + 2 < $m; $j++) {
                $region = true;
                for ($k = 0; $k < 3; $k++) {
                    for ($l = 0; $l < 2; $l++) {
                        $region = $region && abs($image[$i + $k][$j + $l] - $image[$i + $k][$j + $l + 1]) <= $threshold;
                    }
                }
                for ($k = 0; $k < 2; $k++) {
                    for ($l = 0; $l < 3; $l++) {
                        $region = $region && abs($image[$i + $k][$j + $l] - $image[$i + $k + 1][$j + $l]) <= $threshold;
                    }
                }
                if ($region) {
                    $tot = 0;
                    for ($k = 0; $k < 3; $k++) {
                        for ($l = 0; $l < 3; $l++) $tot += $image[$i + $k][$j + $l];
                    }
                    for ($k = 0; $k < 3; $k++) {
                        for ($l = 0; $l < 3; $l++) {
                            $ct[$i + $k][$j + $l]++;
                            $ans[$i + $k][$j + $l] += intdiv($tot, 9);
                        }
                    }
                }
            }
        }
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                if ($ct[$i][$j] === 0) $ans[$i][$j] = $image[$i][$j];
                else $ans[$i][$j] = intdiv($ans[$i][$j], $ct[$i][$j]);
            }
        }
        return $ans;
    }
}
