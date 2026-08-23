// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot {
    private final int w, h, peri;
    private int pos = 0;
    private boolean moved = false;

    public Robot(int width, int height) {
        w = width;
        h = height;
        peri = 2 * (width + height) - 4;
    }

    private int[] getPosDir() {
        // returns x, y, dirCode: 0 East 1 North 2 West 3 South
        int p = pos;
        if (p == 0) {
            if (!moved) return new int[] { 0, 0, 0 };
            return new int[] { 0, 0, 3 };
        }
        if (p <= w - 1) return new int[] { p, 0, 0 };
        p -= w - 1;
        if (p <= h - 1) return new int[] { w - 1, p, 1 };
        p -= h - 1;
        if (p <= w - 1) return new int[] { w - 1 - p, h - 1, 2 };
        p -= w - 1;
        return new int[] { 0, h - 1 - p, 3 };
    }

    public void step(int num) {
        moved = true;
        pos = (pos + num) % peri;
    }

    public int[] getPos() {
        int[] pd = getPosDir();
        return new int[] { pd[0], pd[1] };
    }

    public String getDir() {
        String[] names = { "East", "North", "West", "South" };
        return names[getPosDir()[2]];
    }
}
