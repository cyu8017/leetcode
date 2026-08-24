<?php
// LeetCode 3257 - Maximum Value Sum by Placing Three Rooks II
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

class Solution {
    function maximumValueSum($board) {
        $m = count($board);
        $n = count($board[0]);
        $tops = [];
        for ($i = 0; $i < $m; $i++) {
            $row = [];
            for ($j = 0; $j < $n; $j++) {
                $cur = [$board[$i][$j], $j];
                $placed = false;
                for ($t = 0; $t < count($row); $t++) {
                    if ($cur[0] > $row[$t][0]) {
                        array_splice($row, $t, 0, [$cur]);
                        $placed = true;
                        break;
                    }
                }
                if (!$placed) $row[] = $cur;
                if (count($row) > 3) $row = array_slice($row, 0, 3);
            }
            $tops[] = $row;
        }
        $ans = PHP_INT_MIN;
        for ($i = 0; $i < $m; $i++) {
            foreach ($tops[$i] as $a) {
                for ($j = $i + 1; $j < $m; $j++) {
                    foreach ($tops[$j] as $b) {
                        if ($a[1] === $b[1]) continue;
                        for ($k = $j + 1; $k < $m; $k++) {
                            foreach ($tops[$k] as $c) {
                                if ($c[1] === $a[1] || $c[1] === $b[1]) continue;
                                $s = $a[0] + $b[0] + $c[0];
                                if ($s > $ans) $ans = $s;
                            }
                        }
                    }
                }
            }
        }
        return $ans;
    }
}
