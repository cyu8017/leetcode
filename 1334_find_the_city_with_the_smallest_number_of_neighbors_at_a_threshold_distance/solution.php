<?php
class Solution {
    function findTheCity($n, $edges, $distanceThreshold) {
        $inf = 10 ** 15;
        $dist = array_fill(0, $n, array_fill(0, $n, $inf));
        for ($i = 0; $i < $n; $i++) $dist[$i][$i] = 0;
        foreach ($edges as [$a, $b, $weight]) {
            $dist[$a][$b] = $weight;
            $dist[$b][$a] = $weight;
        }
        for ($k = 0; $k < $n; $k++) {
            for ($i = 0; $i < $n; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    $dist[$i][$j] = min($dist[$i][$j], $dist[$i][$k] + $dist[$k][$j]);
                }
            }
        }
        $bestCity = 0;
        $bestCount = $n;
        for ($city = 0; $city < $n; $city++) {
            $count = 0;
            foreach ($dist[$city] as $d) {
                if ($d <= $distanceThreshold) $count++;
            }
            if ($count < $bestCount || ($count === $bestCount && $city > $bestCity)) {
                $bestCount = $count;
                $bestCity = $city;
            }
        }
        return $bestCity;
    }
}
