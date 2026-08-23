// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

using System;
using System.Collections.Generic;

public class Solution {
    public int Racecar(int target) {
        var queue = new Queue<(int pos, int speed, int steps)>();
        queue.Enqueue((0, 1, 0));
        var seen = new HashSet<long>();
        long Key(int pos, int speed) => ((long)pos << 20) ^ ((uint)speed & 0xfffff);
        seen.Add(Key(0, 1));
        while (queue.Count > 0) {
            var (pos, speed, steps) = queue.Dequeue();
            if (pos == target) return steps;
            int nxtPos = pos + speed, nxtSpeed = speed * 2;
            if (!seen.Contains(Key(nxtPos, nxtSpeed)) && Math.Abs(nxtPos) < target * 2) {
                seen.Add(Key(nxtPos, nxtSpeed));
                queue.Enqueue((nxtPos, nxtSpeed, steps + 1));
            }
            int revSpeed = speed > 0 ? -1 : 1;
            if (seen.Add(Key(pos, revSpeed))) queue.Enqueue((pos, revSpeed, steps + 1));
        }
        return -1;
    }
}
