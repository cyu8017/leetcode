// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

class Bitset {
    private final char[] bits;
    private int ones = 0;
    private boolean flipped = false;
    private final int size;

    public Bitset(int size) {
        this.size = size;
        bits = new char[size];
    }

    public void fix(int idx) {
        char target = flipped ? (char) 0 : (char) 1;
        if (bits[idx] != target) {
            bits[idx] = target;
            ones += flipped ? -1 : 1;
        }
    }

    public void unfix(int idx) {
        char target = flipped ? (char) 1 : (char) 0;
        if (bits[idx] != target) {
            bits[idx] = target;
            ones += flipped ? 1 : -1;
        }
    }

    public void flip() {
        flipped = !flipped;
        ones = size - ones;
    }

    public boolean all() { return ones == size; }
    public boolean one() { return ones > 0; }
    public int count() { return ones; }

    @Override
    public String toString() {
        char[] b = new char[size];
        for (int i = 0; i < size; i++) {
            char v = bits[i];
            if (flipped) v = (char) (v ^ 1);
            b[i] = (char) ('0' + v);
        }
        return new String(b);
    }
}
