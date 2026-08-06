<?php
class Solution {
    function peopleIndexes($favoriteCompanies) {
        $sets = [];
        foreach ($favoriteCompanies as $x) $sets[] = array_flip($x);
        $answer = [];
        $n = count($sets);
        for ($i = 0; $i < $n; $i++) {
            $subset = false;
            for ($j = 0; $j < $n; $j++) {
                if ($i === $j) continue;
                $ok = true;
                foreach ($sets[$i] as $c => $_) {
                    if (!isset($sets[$j][$c])) { $ok = false; break; }
                }
                if ($ok) { $subset = true; break; }
            }
            if (!$subset) $answer[] = $i;
        }
        return $answer;
    }
}
