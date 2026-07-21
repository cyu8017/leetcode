// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

public class FindSumPairs {
    private readonly int[] nums1;
    private readonly int[] nums2;
    private readonly Dictionary<int, int> counts = new();

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums1 = nums1;
        this.nums2 = (int[])nums2.Clone();
        foreach (int num in this.nums2) {
            counts[num] = counts.GetValueOrDefault(num) + 1;
        }
    }

    public void Add(int index, int val) {
        counts[nums2[index]]--;
        nums2[index] += val;
        counts[nums2[index]] = counts.GetValueOrDefault(nums2[index]) + 1;
    }

    public int Count(int tot) {
        int answer = 0;
        foreach (int num in nums1) {
            answer += counts.GetValueOrDefault(tot - num);
        }
        return answer;
    }
}
