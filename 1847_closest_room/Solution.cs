// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] ClosestRoom(int[][] rooms, int[][] queries) {
        Array.Sort(rooms, (a, b) => a[1].CompareTo(b[1]));
        var indexed = new int[queries.Length][];
        for (int i = 0; i < queries.Length; i++) {
            indexed[i] = new[] { i, queries[i][0], queries[i][1] };
        }
        Array.Sort(indexed, (a, b) => b[2].CompareTo(a[2]));

        var available = new SortedSet<int>();
        int roomIndex = rooms.Length - 1;
        int[] answer = new int[queries.Length];
        Array.Fill(answer, -1);

        foreach (var query in indexed) {
            int queryIndex = query[0], preferred = query[1], minSize = query[2];
            while (roomIndex >= 0 && rooms[roomIndex][1] >= minSize) {
                available.Add(rooms[roomIndex][0]);
                roomIndex--;
            }
            if (available.Count == 0) continue;

            int bestId = -1, bestDist = int.MaxValue;
            var higherView = available.GetViewBetween(preferred, int.MaxValue);
            if (higherView.Count > 0) {
                bestId = higherView.Min;
                bestDist = Math.Abs(bestId - preferred);
            }
            if (preferred > int.MinValue) {
                var lowerView = available.GetViewBetween(int.MinValue, preferred);
                if (lowerView.Count > 0) {
                    int lower = lowerView.Max;
                    int dist = Math.Abs(lower - preferred);
                    if (dist < bestDist || (dist == bestDist && lower < bestId)) {
                        bestId = lower;
                    }
                }
            }
            answer[queryIndex] = bestId;
        }
        return answer;
    }
}
