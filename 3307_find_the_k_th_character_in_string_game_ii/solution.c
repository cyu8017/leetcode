// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

char kthCharacter(long long k, int* operations, int operationsSize) {
    int shift = 0;
    int n = operationsSize;
    while (n > 0) {
        int op = operations[n - 1];
        n--;
        long long half = 1LL << n;
        if (k > half) {
            k -= half;
            if (op == 1) shift++;
        }
    }
    return (char)('a' + shift % 26);
}
