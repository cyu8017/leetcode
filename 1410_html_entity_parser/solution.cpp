#include <string>
#include <vector>
#include <utility>

class Solution {
public:
    std::string entityParser(std::string text) {
        // Replace longer entities first; &amp; last to avoid double-decode issues
        // Python replaces &quot; first then ... &amp; last in dict order py3.7+
        // Actually Python iterates dict insertion order: quot,apos,amp,gt,lt,frasl
        // So &amp; is replaced before later ones - but amp appears in others!
        // Wait - they replace &quot; etc first, then &amp;. Good.
        // But if we replace &amp; first we'd break &amp;quot; -> &quot; -> "
        // Python order: quot,apos,amp,gt,lt,frasl - so amp is mid. That could turn &amp;gt; into &> then stuck?
        // &amp;gt; -> after amp replace: &>gt; - wrong!
        // Actually LeetCode wants &amp;gt; -> &gt; (amp first in some sols) OR replace amp last.
        // Standard solution: replace amp last.
        std::vector<std::pair<std::string, std::string>> entities = {
            {"&quot;", "\""}, {"&apos;", "'"}, {"&gt;", ">"},
            {"&lt;", "<"}, {"&frasl;", "/"}, {"&amp;", "&"}
        };
        std::string result;
        for (size_t i = 0; i < text.size(); ) {
            if (text[i] == '&') {
                bool matched = false;
                for (auto& [enc, dec] : entities) {
                    if (text.compare(i, enc.size(), enc) == 0) {
                        result += dec;
                        i += enc.size();
                        matched = true;
                        break;
                    }
                }
                if (!matched) result.push_back(text[i++]);
            } else result.push_back(text[i++]);
        }
        return result;
    }
};
