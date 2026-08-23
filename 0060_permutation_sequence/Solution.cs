// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

public class Solution {
    public string GetPermutation(int n, int k) {
        var numbers = new List<int>();
        var factorials = new int[n];
        factorials[0] = 1;

        for (int i = 0; i < n; i++) {
            numbers.Add(i + 1);
            if (i > 0) {
                factorials[i] = factorials[i - 1] * i;
            }
        }

        k--;
        var result = new System.Text.StringBuilder();

        for (int i = n - 1; i >= 0; i--) {
            int index = k / factorials[i];
            result.Append(numbers[index]);
            numbers.RemoveAt(index);
            k %= factorials[i];
        }

        return result.ToString();
    }
}
