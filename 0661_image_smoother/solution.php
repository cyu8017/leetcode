<?php
// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/

class Solution {
    function imageSmoother($img) {
        $m = count($img);
        $n = count($img[0]);
        $out = [];
        for ($i = 0; $i < $m; ++$i) $out[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $total = 0;
                $count = 0;
                for ($di = -1; $di <= 1; ++$di) {
                    for ($dj = -1; $dj <= 1; ++$dj) {
                        $ni = $i + $di;
                        $nj = $j + $dj;
                        if ($ni >= 0 && $ni < $m && $nj >= 0 && $nj < $n) {
                            $total += $img[$ni][$nj];
                            ++$count;
                        }
                    }
                }
                $out[$i][$j] = intdiv($total, $count);
            }
        }
        return $out;
    }
}
