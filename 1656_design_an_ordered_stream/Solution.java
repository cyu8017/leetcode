// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

import java.util.ArrayList;
import java.util.List;

class OrderedStream {
    private final String[] stream;
    private int ptr = 1;

    public OrderedStream(int n) {
        stream = new String[n + 1];
    }

    public String[] insert(int idKey, String value) {
        stream[idKey] = value;
        List<String> out = new ArrayList<>();
        while (ptr < stream.length && stream[ptr] != null) {
            out.add(stream[ptr]);
            ptr++;
        }
        return out.toArray(new String[0]);
    }
}
