// LeetCode 1535 - Find the Winner of an Array Game
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

int getWinner(int* arr, int arrSize, int k) {
    int champion = arr[0], wins = 0;
    for (int i = 1; i < arrSize; i++) {
        if (champion > arr[i]) {
            wins++;
        } else {
            champion = arr[i];
            wins = 1;
        }
        if (wins == k) break;
    }
    return champion;
}
