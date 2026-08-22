// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

int findTheWinner(int n, int k) {
    int pos = 0;
    for (int size = 2; size <= n; size++) {
        pos = (pos + k) % size;
    }
    return pos + 1;
}
