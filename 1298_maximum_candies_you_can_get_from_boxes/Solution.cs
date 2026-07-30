// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

using System.Collections.Generic;

public class Solution {
    public int MaxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        var owned = new HashSet<int>(initialBoxes);
        var opened = new HashSet<int>();
        var queue = new Queue<int>();
        foreach (int box in initialBoxes) {
            if (status[box] == 1) queue.Enqueue(box);
        }
        int total = 0;
        while (queue.Count > 0) {
            int box = queue.Dequeue();
            if (opened.Contains(box) || status[box] == 0) continue;
            opened.Add(box);
            total += candies[box];
            foreach (int key in keys[box]) {
                status[key] = 1;
                if (owned.Contains(key) && !opened.Contains(key)) queue.Enqueue(key);
            }
            foreach (int child in containedBoxes[box]) {
                owned.Add(child);
                if (status[child] == 1 && !opened.Contains(child)) queue.Enqueue(child);
            }
        }
        return total;
    }
}
