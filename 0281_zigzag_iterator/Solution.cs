// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

public class ZigzagIterator {
    private int[][] vectors;
    private int[] indices;
    private int turn;

    public ZigzagIterator(int[] v1, int[] v2) {
        vectors = new[] { v1, v2 };
        indices = new int[2];
        turn = 0;
    }

    public int Next() {
        while (indices[turn] >= vectors[turn].Length) {
            turn = 1 - turn;
        }
        int value = vectors[turn][indices[turn]];
        indices[turn]++;
        turn = 1 - turn;
        return value;
    }

    public bool HasNext() {
        for (int index = 0; index < vectors.Length; index++) {
            if (indices[index] < vectors[index].Length) {
                return true;
            }
        }
        return false;
    }
}
