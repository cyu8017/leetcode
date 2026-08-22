// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

static int score2660(int* p, int n) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        int mul = 1;
        if ((i > 0 && p[i - 1] == 10) || (i > 1 && p[i - 2] == 10)) mul = 2;
        s += mul * p[i];
    }
    return s;
}

int isWinner(int* player1, int player1Size, int* player2, int player2Size) {
    int a = score2660(player1, player1Size);
    int b = score2660(player2, player2Size);
    if (a > b) return 1;
    if (b > a) return 2;
    return 0;
}
