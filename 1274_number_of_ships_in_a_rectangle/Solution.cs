// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

public class Point {
    public int x;
    public int y;
    public Point() { }
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Sea {
    public bool HasShips(Point topRight, Point bottomLeft) {
        throw new System.NotImplementedException();
    }
}

public class Solution {
    public int CountShips(Sea sea, Point topRight, Point bottomLeft) {
        if (topRight.x < bottomLeft.x || topRight.y < bottomLeft.y) return 0;
        if (!sea.HasShips(topRight, bottomLeft)) return 0;
        if (topRight.x == bottomLeft.x && topRight.y == bottomLeft.y) return 1;
        int mx = (topRight.x + bottomLeft.x) / 2;
        int my = (topRight.y + bottomLeft.y) / 2;
        return CountShips(sea, new Point(mx, my), bottomLeft)
            + CountShips(sea, new Point(topRight.x, my), new Point(mx + 1, bottomLeft.y))
            + CountShips(sea, new Point(mx, topRight.y), new Point(bottomLeft.x, my + 1))
            + CountShips(sea, topRight, new Point(mx + 1, my + 1));
    }
}
