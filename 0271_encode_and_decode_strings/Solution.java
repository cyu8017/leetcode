// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

import java.util.ArrayList;
import java.util.List;

class Codec {
    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String text : strs) {
            encoded.append(text.length()).append('#').append(text);
        }
        return encoded.toString();
    }

    public List<String> decode(String encoded) {
        List<String> result = new ArrayList<>();
        int index = 0;
        while (index < encoded.length()) {
            int delimiter = encoded.indexOf('#', index);
            int length = Integer.parseInt(encoded.substring(index, delimiter));
            int start = delimiter + 1;
            result.add(encoded.substring(start, start + length));
            index = start + length;
        }
        return result;
    }
}
