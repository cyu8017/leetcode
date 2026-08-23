// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

public class Bitset {
    private readonly char[] bits;
    private int ones = 0;
    private bool flipped = false;
    private readonly int size;

    public Bitset(int size) {
        this.size = size;
        bits = new char[size];
    }

    public void Fix(int idx) {
        char target = flipped ? (char)0 : (char)1;
        if (bits[idx] != target) {
            bits[idx] = target;
            ones += flipped ? -1 : 1;
        }
    }

    public void Unfix(int idx) {
        char target = flipped ? (char)1 : (char)0;
        if (bits[idx] != target) {
            bits[idx] = target;
            ones += flipped ? 1 : -1;
        }
    }

    public void Flip() {
        flipped = !flipped;
        ones = size - ones;
    }

    public bool All() { return ones == size; }
    public bool One() { return ones > 0; }
    public int Count() { return ones; }

    public override string ToString() {
        char[] b = new char[size];
        for (int i = 0; i < size; i++) {
            char v = bits[i];
            if (flipped) v = (char)(v ^ 1);
            b[i] = (char)('0' + v);
        }
        return new string(b);
    }
}
