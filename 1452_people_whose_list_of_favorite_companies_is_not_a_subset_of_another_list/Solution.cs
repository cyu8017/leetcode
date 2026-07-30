// LeetCode 1452 - People Whose List Of Favorite Companies Is Not A Subset Of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public IList<int> PeopleIndexes(IList<IList<string>> favoriteCompanies) {
        var sets = favoriteCompanies.Select(x => new HashSet<string>(x)).ToList();
        var answer = new List<int>();
        for (int i = 0; i < sets.Count; i++) {
            bool subset = false;
            for (int j = 0; j < sets.Count; j++)
                if (i != j && sets[i].IsSubsetOf(sets[j])) { subset = true; break; }
            if (!subset) answer.Add(i);
        }
        return answer;
    }
}
