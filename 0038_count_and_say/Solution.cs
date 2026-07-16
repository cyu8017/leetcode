// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

public class Solution {
    public string CountAndSay(int n) {
        string term = "1";

        for (int i = 1; i < n; i++) {
            var nextTerm = new List<char>();
            int index = 0;
            while (index < term.Length) {
                int count = 1;
                while (index + count < term.Length && term[index + count] == term[index]) {
                    count++;
                }
                nextTerm.Add((char)('0' + count));
                nextTerm.Add(term[index]);
                index += count;
            }
            term = new string(nextTerm.ToArray());
        }

        return term;
    }
}
