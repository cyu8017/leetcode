// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

public class Allocator {
    private int[] mem;

    public Allocator(int n) {
        mem = new int[n];
    }

    public int Allocate(int size, int mID) {
        int freeCnt = 0;
        for (int i = 0; i < mem.Length; i++) {
            if (mem[i] == 0) {
                freeCnt++;
                if (freeCnt == size) {
                    int start = i - size + 1;
                    for (int j = start; j <= i; j++) mem[j] = mID;
                    return start;
                }
            } else {
                freeCnt = 0;
            }
        }
        return -1;
    }

    public int FreeMemory(int mID) {
        int cnt = 0;
        for (int i = 0; i < mem.Length; i++) {
            if (mem[i] == mID) {
                mem[i] = 0;
                cnt++;
            }
        }
        return cnt;
    }
}
