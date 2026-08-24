// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class LogSystem {
    private final List<int[]> ids = new ArrayList<>();
    private final List<String> timestamps = new ArrayList<>();
    private final Map<String, Integer> granularityIndex = new HashMap<>();

    public LogSystem() {
        granularityIndex.put("Year", 4);
        granularityIndex.put("Month", 7);
        granularityIndex.put("Day", 10);
        granularityIndex.put("Hour", 13);
        granularityIndex.put("Minute", 16);
        granularityIndex.put("Second", 19);
    }

    public void put(int id, String timestamp) {
        ids.add(new int[] {id});
        timestamps.add(timestamp);
    }

    public List<Integer> retrieve(String start, String end, String granularity) {
        int index = granularityIndex.get(granularity);
        String startKey = start.substring(0, index);
        String endKey = end.substring(0, index);
        List<String[]> matched = new ArrayList<>();
        for (int i = 0; i < timestamps.size(); ++i) {
            String timestamp = timestamps.get(i);
            String key = timestamp.substring(0, index);
            if (startKey.compareTo(key) <= 0 && key.compareTo(endKey) <= 0) {
                matched.add(new String[] {timestamp, String.valueOf(ids.get(i)[0])});
            }
        }
        Collections.sort(matched, (a, b) -> a[0].compareTo(b[0]));
        List<Integer> result = new ArrayList<>();
        for (String[] item : matched) {
            result.add(Integer.parseInt(item[1]));
        }
        return result;
    }
}
