<?php
class UndergroundSystem {
    private $ins = [];
    private $stats = [];

    function __construct() {
        $this->ins = [];
        $this->stats = [];
    }

    function checkIn($id, $stationName, $t) {
        $this->ins[$id] = [$stationName, $t];
    }

    function checkOut($id, $stationName, $t) {
        [$start, $begin] = $this->ins[$id];
        unset($this->ins[$id]);
        $key = $start . "|" . $stationName;
        [$total, $count] = $this->stats[$key] ?? [0, 0];
        $this->stats[$key] = [$total + $t - $begin, $count + 1];
    }

    function getAverageTime($startStation, $endStation) {
        [$total, $count] = $this->stats[$startStation . "|" . $endStation];
        return $total / $count;
    }
}
