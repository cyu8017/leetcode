// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

class Solution {
    private int xCorner;
    private int yCorner;
    private int[][] circles;
    private boolean[] vis;
    private int n;

    public boolean canReachCorner(int xCorner, int yCorner, int[][] circles) {
        this.xCorner = xCorner;
        this.yCorner = yCorner;
        this.circles = circles;
        n = circles.length;
        vis = new boolean[n];
        for (int i = 0; i < n; i++) {
            int x = circles[i][0], y = circles[i][1], r = circles[i][2];
            if (inCircle(0, 0, x, y, r) || inCircle(xCorner, yCorner, x, y, r)) {
                return false;
            }
            if (!vis[i] && crossLeftTop(x, y, r) && dfs(i)) {
                return false;
            }
        }
        return true;
    }

    private boolean inCircle(int x, int y, int cx, int cy, int r) {
        long dx = x - cx, dy = y - cy;
        return dx * dx + dy * dy <= (long) r * r;
    }

    private boolean crossLeftTop(int cx, int cy, int r) {
        boolean a = Math.abs(cx) <= r && cy >= 0 && cy <= yCorner;
        boolean b = Math.abs(cy - yCorner) <= r && cx >= 0 && cx <= xCorner;
        return a || b;
    }

    private boolean crossRightBottom(int cx, int cy, int r) {
        boolean a = Math.abs(cx - xCorner) <= r && cy >= 0 && cy <= yCorner;
        boolean b = Math.abs(cy) <= r && cx >= 0 && cx <= xCorner;
        return a || b;
    }

    private boolean dfs(int i) {
        int x1 = circles[i][0], y1 = circles[i][1], r1 = circles[i][2];
        if (crossRightBottom(x1, y1, r1)) {
            return true;
        }
        vis[i] = true;
        for (int j = 0; j < n; j++) {
            if (vis[j]) {
                continue;
            }
            int x2 = circles[j][0], y2 = circles[j][1], r2 = circles[j][2];
            if ((long) (x1 - x2) * (x1 - x2) + (long) (y1 - y2) * (y1 - y2) > (long) (r1 + r2) * (r1 + r2)) {
                continue;
            }
            if ((long) x1 * r2 + (long) x2 * r1 < (long) (r1 + r2) * xCorner
                    && (long) y1 * r2 + (long) y2 * r1 < (long) (r1 + r2) * yCorner
                    && dfs(j)) {
                return true;
            }
        }
        return false;
    }
}
