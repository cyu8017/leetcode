// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

public class Robot {
    private readonly int w, h, peri;
    private int pos = 0;
    private bool moved = false;

    public Robot(int width, int height) {
        w = width; h = height; peri = 2 * (width + height) - 4;
    }

    private (int x, int y, string d) GetPosDir() {
        int p = pos;
        if (p == 0) {
            if (!moved) return (0, 0, "East");
            return (0, 0, "South");
        }
        if (p <= w - 1) return (p, 0, "East");
        p -= w - 1;
        if (p <= h - 1) return (w - 1, p, "North");
        p -= h - 1;
        if (p <= w - 1) return (w - 1 - p, h - 1, "West");
        p -= w - 1;
        return (0, h - 1 - p, "South");
    }

    public void Step(int num) {
        moved = true;
        pos = (pos + num) % peri;
    }

    public int[] GetPos() {
        var (x, y, _) = GetPosDir();
        return new[] { x, y };
    }

    public string GetDir() {
        var (_, _, d) = GetPosDir();
        return d;
    }
}
