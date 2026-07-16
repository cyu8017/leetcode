// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

class Solution {
    /**
     * @param Integer[][] $intervals
     * @return Boolean
     */
    function canAttendMeetings($intervals) {
        usort($intervals, function ($left, $right) {
            return $left[0] <=> $right[0];
        });

        for ($index = 1; $index < count($intervals); $index++) {
            if ($intervals[$index][0] < $intervals[$index - 1][1]) {
                return false;
            }
        }

        return true;
    }
}
