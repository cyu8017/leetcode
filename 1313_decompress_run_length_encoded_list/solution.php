<?php
class Solution {
    function decompressRLElist($nums) {
        $answer = [];
        for ($i = 0; $i < count($nums); $i += 2) {
            for ($j = 0; $j < $nums[$i]; $j++) $answer[] = $nums[$i + 1];
        }
        return $answer;
    }
}
