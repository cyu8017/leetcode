// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

using System.Collections.Generic;

public class Solution {
    public bool CanVisitAllRooms(IList<IList<int>> rooms) {
        var seen = new HashSet<int> { 0 };
        var stack = new List<int> { 0 };
        while (stack.Count > 0) {
            int room = stack[stack.Count - 1];
            stack.RemoveAt(stack.Count - 1);
            foreach (int key in rooms[room])
                if (seen.Add(key)) stack.Add(key);
        }
        return seen.Count == rooms.Count;
    }
}
