<?php
class Solution {
    function simplifiedFractions($n) {
        $answer = [];
        for ($a = 1; $a < $n; $a++) {
            for ($b = $a + 1; $b <= $n; $b++) {
                if ($this->gcd($a, $b) === 1) $answer[] = "$a/$b";
            }
        }
        return $answer;
    }
    private function gcd($a, $b) {
        while ($b) {
            $t = $a % $b;
            $a = $b;
            $b = $t;
        }
        return $a;
    }
}
