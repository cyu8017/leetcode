// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

class Sea {
    public boolean hasShips(int[] topRight, int[] bottomLeft) {
        throw new UnsupportedOperationException();
    }
}

class Solution {
    public int countShips(Sea sea, int[] topRight, int[] bottomLeft) {
        int tx = topRight[0], ty = topRight[1];
        int bx = bottomLeft[0], by = bottomLeft[1];
        if (tx < bx || ty < by || !sea.hasShips(topRight, bottomLeft)) return 0;
        if (tx == bx && ty == by) return 1;
        int mx = (tx + bx) / 2, my = (ty + by) / 2;
        return countShips(sea, new int[] { mx, my }, bottomLeft)
            + countShips(sea, new int[] { tx, my }, new int[] { mx + 1, by })
            + countShips(sea, new int[] { mx, ty }, new int[] { bx, my + 1 })
            + countShips(sea, topRight, new int[] { mx + 1, my + 1 });
    }
}
