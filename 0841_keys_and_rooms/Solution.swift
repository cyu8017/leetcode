// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

class Solution {
    func canVisitAllRooms(_ rooms: [[Int]]) -> Bool {
        var seen: Set<Int> = [0]
        var stack = [0]
        while !stack.isEmpty {
            let room = stack.removeLast()
            for key in rooms[room] where seen.insert(key).inserted {
                stack.append(key)
            }
        }
        return seen.count == rooms.count
    }
}
