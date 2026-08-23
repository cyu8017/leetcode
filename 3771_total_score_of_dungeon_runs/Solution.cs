// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

public class Solution {
    public long TotalScore(int hp, int[] damage, int[] requirement) {
        int n = damage.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + damage[i];
        long answer = 1L * n * (n + 1) / 2;
        for (int j = 1; j <= n; j++) {
            long threshold = prefix[j] + (requirement[j - 1] - hp);
            int lo = 0, hi = j;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (prefix[mid] < threshold) lo = mid + 1;
                else hi = mid;
            }
            answer -= lo;
        }
        return answer;
    }
}
