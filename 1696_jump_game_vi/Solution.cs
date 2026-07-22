// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

using System.Collections.Generic;

public class Solution {
    public int MaxResult(int[] nums, int k) {
        var q = new LinkedList<(int idx, int score)>();
        q.AddLast((0, nums[0]));
        for (int i = 1; i < nums.Length; i++) {
            while (q.Count > 0 && q.First.Value.idx < i - k) q.RemoveFirst();
            int score = nums[i] + q.First.Value.score;
            while (q.Count > 0 && q.Last.Value.score <= score) q.RemoveLast();
            q.AddLast((i, score));
        }
        return q.Last.Value.score;
    }
}
