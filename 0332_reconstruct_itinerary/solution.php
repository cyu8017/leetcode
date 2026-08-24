<?php
// LeetCode 0332 - Reconstruct Itinerary
// https://leetcode.com/problems/reconstruct-itinerary/

class Solution {
    /**
     * @param String[][] $tickets
     * @return String[]
     */
    function findItinerary($tickets) {
        return $this->find_itinerary($tickets);
    }

    /**
     * @param String[][] $tickets
     * @return String[]
     */
    function find_itinerary($tickets) {
        $targets = [];
        usort($tickets, function ($left, $right) {
            return strcmp($left[0], $right[0]) ?: strcmp($left[1], $right[1]);
        });
        for ($index = count($tickets) - 1; $index >= 0; $index--) {
            $source = $tickets[$index][0];
            $destination = $tickets[$index][1];
            if (!array_key_exists($source, $targets)) {
                $targets[$source] = [];
            }
            $targets[$source][] = $destination;
        }

        $route = [];
        $visit = function ($airport) use (&$visit, &$targets, &$route) {
            while (!empty($targets[$airport])) {
                $visit(array_pop($targets[$airport]));
            }
            $route[] = $airport;
        };

        $visit("JFK");
        return array_reverse($route);
    }
}
