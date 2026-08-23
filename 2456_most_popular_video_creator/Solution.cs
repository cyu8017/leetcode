// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

using System.Collections.Generic;

public class Solution {
    private class Info {
        public long Total;
        public string BestID;
        public int BestViews;
    }

    public IList<IList<string>> MostPopularCreator(string[] creators, string[] ids, int[] views) {
        var mp = new Dictionary<string, Info>();
        long maxTotal = 0;
        for (int i = 0; i < creators.Length; i++) {
            if (!mp.ContainsKey(creators[i])) {
                mp[creators[i]] = new Info { Total = views[i], BestID = ids[i], BestViews = views[i] };
            } else {
                var inf = mp[creators[i]];
                inf.Total += views[i];
                if (views[i] > inf.BestViews || (views[i] == inf.BestViews && string.CompareOrdinal(ids[i], inf.BestID) < 0)) {
                    inf.BestViews = views[i];
                    inf.BestID = ids[i];
                }
            }
            if (mp[creators[i]].Total > maxTotal) maxTotal = mp[creators[i]].Total;
        }
        var ans = new List<IList<string>>();
        foreach (var kv in mp) {
            if (kv.Value.Total == maxTotal)
                ans.Add(new List<string> { kv.Key, kv.Value.BestID });
        }
        return ans;
    }
}
