// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

class Solution {
    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function minMeetingRooms($intervals) {
        $starts = array_column($intervals, 0);
        $ends = array_column($intervals, 1);
        sort($starts);
        sort($ends);

        $rooms = 0;
        $maxRooms = 0;
        $startIndex = 0;
        $endIndex = 0;
        while ($startIndex < count($starts)) {
            if ($starts[$startIndex] < $ends[$endIndex]) {
                $rooms += 1;
                $maxRooms = max($maxRooms, $rooms);
                $startIndex += 1;
            } else {
                $rooms -= 1;
                $endIndex += 1;
            }
        }

        return $maxRooms;
    }
}
