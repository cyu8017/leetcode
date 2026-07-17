<?php
// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

class Solution {
    /**
     * @param String[] $features
     * @param String[] $responses
     * @return String[]
     */
    function sortFeatures($features, $responses) {
        $featureSet = array_flip($features);
        $count = [];
        foreach ($responses as $response) {
            $seen = [];
            foreach (preg_split('/\s+/', $response, -1, PREG_SPLIT_NO_EMPTY) as $word) {
                if (isset($featureSet[$word])) {
                    $seen[$word] = true;
                }
            }
            foreach (array_keys($seen) as $word) {
                $count[$word] = ($count[$word] ?? 0) + 1;
            }
        }
        $result = $features;
        usort($result, function ($a, $b) use ($count) {
            $ca = $count[$a] ?? 0;
            $cb = $count[$b] ?? 0;
            if ($ca !== $cb) {
                return $cb - $ca;
            }
            return strcmp($a, $b);
        });
        return $result;
    }
}
