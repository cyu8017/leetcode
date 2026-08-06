<?php
class Solution {
    function longestDiverseString($a, $b, $c) {
        $counts = ["a" => $a, "b" => $b, "c" => $c];
        $answer = "";
        while (true) {
            arsort($counts);
            $picked = false;
            foreach ($counts as $char => $count) {
                if ($count <= 0) continue;
                $len = strlen($answer);
                if ($len >= 2 && $answer[$len - 1] === $char && $answer[$len - 2] === $char) continue;
                $answer .= $char;
                $counts[$char]--;
                $picked = true;
                break;
            }
            if (!$picked) break;
        }
        return $answer;
    }
}
