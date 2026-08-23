// LeetCode 0351 - Android Unlock Patterns

// https://leetcode.com/problems/android-unlock-patterns/



public class Solution {

    private static readonly int[,] Jump = new int[9, 9];



    static Solution() {

        SetJump(0, 2, 1);

        SetJump(2, 0, 1);

        SetJump(0, 6, 3);

        SetJump(6, 0, 3);

        SetJump(0, 8, 4);

        SetJump(8, 0, 4);

        SetJump(2, 8, 5);

        SetJump(8, 2, 5);

        SetJump(2, 6, 7);

        SetJump(6, 2, 7);

        SetJump(6, 8, 7);

        SetJump(8, 6, 7);

        SetJump(1, 7, 8);

        SetJump(7, 1, 8);

        SetJump(3, 7, 6);

        SetJump(7, 3, 6);

        SetJump(1, 5, 4);

        SetJump(5, 1, 4);

        SetJump(3, 5, 5);

        SetJump(5, 3, 5);

        SetJump(1, 3, 2);

        SetJump(3, 1, 2);

        SetJump(4, 5, 5);

        SetJump(5, 4, 5);

        SetJump(4, 7, 8);

        SetJump(7, 4, 8);

        SetJump(4, 3, 5);

        SetJump(3, 4, 5);

        SetJump(4, 1, 2);

        SetJump(1, 4, 2);

        SetJump(4, 6, 7);

        SetJump(6, 4, 7);

        SetJump(4, 8, 6);

        SetJump(8, 4, 6);

        SetJump(4, 0, 2);

        SetJump(0, 4, 2);

        SetJump(4, 2, 6);

        SetJump(2, 4, 6);

    }



    private static void SetJump(int from, int to, int middle) {

        Jump[from, to] = middle;

    }



    public int NumberOfPatterns(int m, int n) {

        return Dfs(1 << 0, 0, 1, m, n) * 4

            + Dfs(1 << 1, 1, 1, m, n) * 4

            + Dfs(1 << 4, 4, 1, m, n);

    }



    private int Dfs(int visited, int last, int length, int m, int n) {

        if (length > n) {

            return 0;

        }



        int count = m <= length && length <= n ? 1 : 0;

        for (int next = 0; next < 9; next++) {

            if (IsValid(visited, last, next)) {

                count += Dfs(visited | (1 << next), next, length + 1, m, n);

            }

        }

        return count;

    }



    private bool IsValid(int visited, int last, int next) {

        if ((visited & (1 << next)) != 0) {

            return false;

        }



        int middle = Jump[last, next];

        if (middle > 0) {

            return (visited & (1 << middle)) == 0;

        }



        return Math.Abs(last / 3 - next / 3) <= 1

            && Math.Abs(last % 3 - next % 3) <= 1;

    }

}
