// LeetCode 1405 - Longest Happy String
// https://leetcode.com/problems/longest-happy-string/

using System.Collections.Generic;
using System.Text;
public class Solution {
    public string LongestDiverseString(int a, int b, int c) {
        var pq = new PriorityQueue<char, int>();
        if (a > 0) pq.Enqueue('a', -a);
        if (b > 0) pq.Enqueue('b', -b);
        if (c > 0) pq.Enqueue('c', -c);
        var answer = new StringBuilder();
        while (pq.Count > 0) {
            pq.TryDequeue(out char ch, out int neg);
            if (answer.Length >= 2 && answer[answer.Length - 1] == ch && answer[answer.Length - 2] == ch) {
                if (pq.Count == 0) break;
                pq.TryDequeue(out char ch2, out int neg2);
                answer.Append(ch2);
                if (neg2 + 1 < 0) pq.Enqueue(ch2, neg2 + 1);
                pq.Enqueue(ch, neg);
            } else {
                answer.Append(ch);
                if (neg + 1 < 0) pq.Enqueue(ch, neg + 1);
            }
        }
        return answer.ToString();
    }
}
