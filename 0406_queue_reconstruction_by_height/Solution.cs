// LeetCode 0406 - Queue Reconstruction by Height

// https://leetcode.com/problems/queue-reconstruction-by-height/



using System.Collections.Generic;

using System.Linq;



public class Solution {

    public int[][] ReconstructQueue(int[][] people) {

        Array.Sort(people, (a, b) => a[0] != b[0]

            ? b[0].CompareTo(a[0])

            : a[1].CompareTo(b[1]));



        List<int[]> queue = new();



        foreach (int[] person in people) {

            queue.Insert(person[1], person);

        }



        return queue.ToArray();

    }

}
