// LeetCode 0391 - Perfect Rectangle

// https://leetcode.com/problems/perfect-rectangle/



import java.util.HashSet;

import java.util.Set;



class Solution {

    public boolean isRectangleCover(int[][] rectangles) {

        Set<Long> points = new HashSet<>();

        long area = 0;

        int minX = Integer.MAX_VALUE;

        int minY = Integer.MAX_VALUE;

        int maxX = Integer.MIN_VALUE;

        int maxY = Integer.MIN_VALUE;



        for (int[] rectangle : rectangles) {

            int x1 = rectangle[0];

            int y1 = rectangle[1];

            int x2 = rectangle[2];

            int y2 = rectangle[3];

            area += (long) (x2 - x1) * (y2 - y1);

            minX = Math.min(minX, x1);

            minY = Math.min(minY, y1);

            maxX = Math.max(maxX, x2);

            maxY = Math.max(maxY, y2);



            int[][] corners = {{x1, y1}, {x1, y2}, {x2, y1}, {x2, y2}};

            for (int[] corner : corners) {

                long point = encode(corner[0], corner[1]);

                if (!points.add(point)) {

                    points.remove(point);

                }

            }

        }



        if (points.size() != 4

                || !points.contains(encode(minX, minY))

                || !points.contains(encode(minX, maxY))

                || !points.contains(encode(maxX, minY))

                || !points.contains(encode(maxX, maxY))) {

            return false;

        }



        return area == (long) (maxX - minX) * (maxY - minY);

    }



    private long encode(int x, int y) {

        return ((long) x << 32) | (y & 0xffffffffL);

    }

}
