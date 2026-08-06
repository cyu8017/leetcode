<?php
class TweetCounts {
    private $times = [];

    function __construct() {
        $this->times = [];
    }

    function recordTweet($tweetName, $time) {
        $this->times[$tweetName][] = $time;
        sort($this->times[$tweetName]);
    }

    function getTweetCountsPerFrequency($freq, $tweetName, $startTime, $endTime) {
        $size = ["minute" => 60, "hour" => 3600, "day" => 86400][$freq];
        $times = $this->times[$tweetName] ?? [];
        $answer = [];
        for ($start = $startTime; $start <= $endTime; $start += $size) {
            $end = min($endTime, $start + $size - 1);
            $count = 0;
            foreach ($times as $t) {
                if ($t >= $start && $t <= $end) $count++;
            }
            $answer[] = $count;
        }
        return $answer;
    }
}
