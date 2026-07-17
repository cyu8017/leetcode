<?php
// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

class Solution {
    /**
     * @param Integer[][] $rooms
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function closestRoom($rooms, $queries) {
        usort($rooms, fn($a, $b) => $a[1] <=> $b[1]);

        $indexedQueries = [];
        foreach ($queries as $index => $query) {
            $indexedQueries[] = [$index, $query];
        }
        usort($indexedQueries, fn($a, $b) => $b[1][1] <=> $a[1][1]);

        $availableIds = [];
        $roomIndex = count($rooms) - 1;
        $answer = array_fill(0, count($queries), -1);

        foreach ($indexedQueries as [$queryIndex, [$preferred, $minSize]]) {
            while ($roomIndex >= 0 && $rooms[$roomIndex][1] >= $minSize) {
                $this->insort($availableIds, $rooms[$roomIndex][0]);
                $roomIndex--;
            }

            if (count($availableIds) === 0) {
                continue;
            }

            $pos = $this->bisectLeft($availableIds, $preferred);
            $bestId = -1;
            $bestDist = PHP_INT_MAX;

            if ($pos < count($availableIds)) {
                $roomId = $availableIds[$pos];
                $dist = abs($roomId - $preferred);
                if ($dist < $bestDist || ($dist === $bestDist && $roomId < $bestId)) {
                    $bestId = $roomId;
                    $bestDist = $dist;
                }
            }

            if ($pos > 0) {
                $roomId = $availableIds[$pos - 1];
                $dist = abs($roomId - $preferred);
                if ($dist < $bestDist || ($dist === $bestDist && $roomId < $bestId)) {
                    $bestId = $roomId;
                }
            }

            $answer[$queryIndex] = $bestId;
        }

        return $answer;
    }

    /**
     * @param int[] $arr
     * @param int $value
     */
    private function insort(&$arr, $value) {
        $pos = $this->bisectLeft($arr, $value);
        array_splice($arr, $pos, 0, [$value]);
    }

    /**
     * @param int[] $arr
     * @param int $value
     * @return int
     */
    private function bisectLeft($arr, $value) {
        $lo = 0;
        $hi = count($arr);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($arr[$mid] < $value) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        return $lo;
    }
}
