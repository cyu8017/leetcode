// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<int>> GroupThePeople(int[] groupSizes) {
        var pending = new Dictionary<int, List<int>>();
        var answer = new List<IList<int>>();
        for (int person = 0; person < groupSizes.Length; person++) {
            int size = groupSizes[person];
            if (!pending.ContainsKey(size)) pending[size] = new List<int>();
            pending[size].Add(person);
            if (pending[size].Count == size) {
                answer.Add(pending[size]);
                pending[size] = new List<int>();
            }
        }
        return answer
            .OrderBy(group => group.Count)
            .ThenBy(group => string.Join(",", group))
            .ToList();
    }
}
