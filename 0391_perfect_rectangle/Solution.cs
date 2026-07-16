// LeetCode 0391 - Perfect Rectangle

// https://leetcode.com/problems/perfect-rectangle/



using System.Collections.Generic;



public class Solution {

    public bool IsRectangleCover(int[][] rectangles) {

        HashSet<long> points = new();

        long area = 0;

        int minX = int.MaxValue;

        int minY = int.MaxValue;

        int maxX = int.MinValue;

        int maxY = int.MinValue;



        foreach (int[] rectangle in rectangles) {

            int x1 = rectangle[0];

            int y1 = rectangle[1];

            int x2 = rectangle[2];

            int y2 = rectangle[3];

            area += (long)(x2 - x1) * (y2 - y1);

            minX = int.Min(minX, x1);

            minY = int.Min(minY, y1);

            maxX = int.Max(maxX, x2);

            maxY = int.Max(maxY, y2);



            int[][] corners = {

                new[] { x1, y1 },

                new[] { x1, y2 },

                new[] { x2, y1 },

                new[] { x2, y2 },

            };

            foreach (int[] corner in corners) {

                long point = Encode(corner[0], corner[1]);

                if (!points.Add(point)) {

                    points.Remove(point);

                }

            }

        }



        if (points.Count != 4

                || !points.Contains(Encode(minX, minY))

                || !points.Contains(Encode(minX, maxY))

                || !points.Contains(Encode(maxX, minY))

                || !points.Contains(Encode(maxX, maxY))) {

            return false;

        }



        return area == (long)(maxX - minX) * (maxY - minY);

    }



    private static long Encode(int x, int y) {

        return ((long)x << 32) | (y & 0xffffffffL);

    }

}
