<?php
class Solution {
    function leftMostColumnWithOne($binaryMatrix) {
        [$rows, $cols] = $binaryMatrix->dimensions();
        $row = 0;
        $col = $cols - 1;
        $answer = -1;
        while ($row < $rows && $col >= 0) {
            if ($binaryMatrix->get($row, $col) === 1) {
                $answer = $col;
                $col--;
            } else {
                $row++;
            }
        }
        return $answer;
    }
}
