<?php
class Solution {
    function diagonalSort($mat) {
        $diagonals = [];
        foreach ($mat as $r => $row) {
            foreach ($row as $c => $value) {
                $diagonals[$r - $c][] = $value;
            }
        }
        foreach ($diagonals as $k => $values) {
            rsort($diagonals[$k]);
        }
        foreach ($mat as $r => $row) {
            foreach ($row as $c => $_) {
                $mat[$r][$c] = array_pop($diagonals[$r - $c]);
            }
        }
        return $mat;
    }
}
