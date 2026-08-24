// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

class Solution {
    fun canVisitAllRooms(rooms: MutableList<MutableList<Int>>): Boolean {
        var seen = HashSet<Int>()
        var stack = ArrayDeque<Int>()
        seen.add(0)
        stack.push(0)
        while (!stack.isEmpty()) {
            var room = stack.pop()
            for (key in rooms[room]) {
                if (seen.add(key)) stack.push(key)
            }
        }
        return seen.size == rooms.size
    }
}
