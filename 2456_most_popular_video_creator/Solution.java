// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private static class Info {
        long total;
        String bestID;
        int bestViews;
        Info(long total, String bestID, int bestViews) {
            this.total = total;
            this.bestID = bestID;
            this.bestViews = bestViews;
        }
    }

    public List<List<String>> mostPopularCreator(String[] creators, String[] ids, int[] views) {
        Map<String, Info> mp = new HashMap<>();
        long maxTotal = 0;
        for (int i = 0; i < creators.length; i++) {
            Info info = mp.get(creators[i]);
            if (info == null) {
                mp.put(creators[i], new Info(views[i], ids[i], views[i]));
            } else {
                info.total += views[i];
                if (views[i] > info.bestViews ||
                    (views[i] == info.bestViews && ids[i].compareTo(info.bestID) < 0)) {
                    info.bestViews = views[i];
                    info.bestID = ids[i];
                }
            }
            maxTotal = Math.max(maxTotal, mp.get(creators[i]).total);
        }
        List<List<String>> ans = new ArrayList<>();
        for (Map.Entry<String, Info> e : mp.entrySet()) {
            if (e.getValue().total == maxTotal) {
                List<String> row = new ArrayList<>();
                row.add(e.getKey());
                row.add(e.getValue().bestID);
                ans.add(row);
            }
        }
        return ans;
    }
}
