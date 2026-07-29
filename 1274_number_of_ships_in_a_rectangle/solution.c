// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

#include <stdbool.h>

typedef struct {
    int x;
    int y;
} Point;

typedef struct Sea Sea;

struct Sea {
    bool (*hasShips)(Sea*, Point, Point);
};

static int countShipsRec(Sea* sea, Point topRight, Point bottomLeft) {
    if (topRight.x < bottomLeft.x || topRight.y < bottomLeft.y) return 0;
    if (!sea->hasShips(sea, topRight, bottomLeft)) return 0;
    if (topRight.x == bottomLeft.x && topRight.y == bottomLeft.y) return 1;
    int mx = (topRight.x + bottomLeft.x) / 2;
    int my = (topRight.y + bottomLeft.y) / 2;
    return countShipsRec(sea, (Point){mx, my}, bottomLeft)
         + countShipsRec(sea, (Point){topRight.x, my}, (Point){mx + 1, bottomLeft.y})
         + countShipsRec(sea, (Point){mx, topRight.y}, (Point){bottomLeft.x, my + 1})
         + countShipsRec(sea, topRight, (Point){mx + 1, my + 1});
}

int countShips(Sea* sea, Point topRight, Point bottomLeft) {
    return countShipsRec(sea, topRight, bottomLeft);
}
