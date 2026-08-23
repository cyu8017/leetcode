// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

class ZigzagIterator {
    private int[][] vectors;
    private int[] indices;
    private int turn;

    public ZigzagIterator(int[] v1, int[] v2) {
        this.vectors = new int[][] { v1, v2 };
        this.indices = new int[] { 0, 0 };
        this.turn = 0;
    }

    public int next() {
        while (indices[turn] >= vectors[turn].length) {
            turn = 1 - turn;
        }
        int value = vectors[turn][indices[turn]];
        indices[turn]++;
        turn = 1 - turn;
        return value;
    }

    public boolean hasNext() {
        for (int index = 0; index < vectors.length; index++) {
            if (indices[index] < vectors[index].length) {
                return true;
            }
        }
        return false;
    }
}
