// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

class Point {
public:
    int x;
    int y;
    Point() : x(0), y(0) {}
    Point(int a, int b) : x(a), y(b) {}
};

class Sea {
public:
    bool hasShips(Point topRight, Point bottomLeft);
};

class Solution {
public:
    int countShips(Sea& sea, Point topRight, Point bottomLeft) {
        if (topRight.x < bottomLeft.x || topRight.y < bottomLeft.y) {
            return 0;
        }
        if (!sea.hasShips(topRight, bottomLeft)) {
            return 0;
        }
        if (topRight.x == bottomLeft.x && topRight.y == bottomLeft.y) {
            return 1;
        }
        int mx = (topRight.x + bottomLeft.x) / 2;
        int my = (topRight.y + bottomLeft.y) / 2;
        return countShips(sea, Point(mx, my), bottomLeft) +
               countShips(sea, Point(topRight.x, my), Point(mx + 1, bottomLeft.y)) +
               countShips(sea, Point(mx, topRight.y), Point(bottomLeft.x, my + 1)) +
               countShips(sea, topRight, Point(mx + 1, my + 1));
    }
};
