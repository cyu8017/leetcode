<?php
// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

class Solution {
    /**
     * @param Integer[][] $encoded1
     * @param Integer[][] $encoded2
     * @return Integer[][]
     */
    function findRLEArray($encoded1, $encoded2) {
        $result = [];
        $i = 0;
        $j = 0;
        $rem1 = $encoded1[0][1];
        $rem2 = $encoded2[0][1];

        while ($i < count($encoded1)) {
            $take = min($rem1, $rem2);
            $value = $encoded1[$i][0] * $encoded2[$j][0];
            if ($result !== [] && $result[count($result) - 1][0] === $value) {
                $result[count($result) - 1][1] += $take;
            } else {
                $result[] = [$value, $take];
            }

            $rem1 -= $take;
            $rem2 -= $take;
            if ($rem1 === 0) {
                $i++;
                if ($i < count($encoded1)) {
                    $rem1 = $encoded1[$i][1];
                }
            }
            if ($rem2 === 0) {
                $j++;
                if ($j < count($encoded2)) {
                    $rem2 = $encoded2[$j][1];
                }
            }
        }

        return $result;
    }
}
