// LeetCode 3248 - Snake in Matrix
// https://leetcode.com/problems/snake-in-matrix/

int finalPositionOfSnake(int n, char** commands, int commandsSize) {
    int x = 0, y = 0;
    for (int i = 0; i < commandsSize; i++) {
        char c = commands[i][0];
        if (c == 'U') x--;
        else if (c == 'D') x++;
        else if (c == 'L') y--;
        else if (c == 'R') y++;
    }
    return x * n + y;
}
