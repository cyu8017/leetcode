<?php

class Solution {
    function maxPoints(array $points): int {
        $count = count($points);
        if ($count <= 2) {
            return $count;
        }

        $best = 1;
        for ($i = 0; $i < $count; $i++) {
            $slopes = [];
            $localBest = 1;
            for ($j = $i + 1; $j < $count; $j++) {
                $dx = $points[$j][0] - $points[$i][0];
                $dy = $points[$j][1] - $points[$i][1];
                $divisor = $this->gcd($dx, $dy);
                $dx = intdiv($dx, $divisor);
                $dy = intdiv($dy, $divisor);
                if ($dx < 0 || ($dx === 0 && $dy < 0)) {
                    $dx = -$dx;
                    $dy = -$dy;
                }

                $slope = "$dx,$dy";
                $slopes[$slope] = ($slopes[$slope] ?? 0) + 1;
                $localBest = max($localBest, $slopes[$slope] + 1);
            }
            $best = max($best, $localBest);
        }
        return $best;
    }

    private function gcd(int $a, int $b): int {
        $a = abs($a);
        $b = abs($b);
        while ($b !== 0) {
            $remainder = $a % $b;
            $a = $b;
            $b = $remainder;
        }
        return $a;
    }
}