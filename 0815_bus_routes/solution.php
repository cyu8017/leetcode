<?php
// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

class Solution {
    /**
     * @param Integer[][] $routes
     * @param Integer $source
     * @param Integer $target
     * @return Integer
     */
    function numBusesToDestination($routes, $source, $target) {
        if ($source === $target) return 0;
        $stopToBuses = [];
        $rn = count($routes);
        for ($bus = 0; $bus < $rn; $bus++) {
            foreach ($routes[$bus] as $stop) {
                if (!isset($stopToBuses[$stop])) $stopToBuses[$stop] = [];
                $stopToBuses[$stop][] = $bus;
            }
        }
        $queue = [[$source, 0]];
        $seenStops = [$source => true];
        $seenBuses = [];
        $qi = 0;
        while ($qi < count($queue)) {
            $stop = $queue[$qi][0];
            $busesTaken = $queue[$qi][1];
            $qi++;
            foreach ($stopToBuses[$stop] ?? [] as $bus) {
                if (isset($seenBuses[$bus])) continue;
                $seenBuses[$bus] = true;
                foreach ($routes[$bus] as $nxt) {
                    if ($nxt === $target) return $busesTaken + 1;
                    if (!isset($seenStops[$nxt])) {
                        $seenStops[$nxt] = true;
                        $queue[] = [$nxt, $busesTaken + 1];
                    }
                }
            }
        }
        return -1;
    }
}
