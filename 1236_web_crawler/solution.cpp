// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class HtmlParser {
public:
    std::vector<std::string> getUrls(std::string url);
};

class Solution {
public:
    std::vector<std::string> crawl(std::string startUrl, HtmlParser* htmlParser) {
        auto hostOf = [](const std::string& url) {
            std::size_t start = url.find("://");
            start = (start == std::string::npos) ? 0 : start + 3;
            std::size_t end = url.find('/', start);
            return url.substr(start, end == std::string::npos ? std::string::npos : end - start);
        };
        const std::string host = hostOf(startUrl);
        std::unordered_set<std::string> seen{startUrl};
        std::vector<std::string> stack{startUrl};
        while (!stack.empty()) {
            std::string url = stack.back();
            stack.pop_back();
            for (const std::string& next : htmlParser->getUrls(url)) {
                if (hostOf(next) == host && !seen.count(next)) {
                    seen.insert(next);
                    stack.push_back(next);
                }
            }
        }
        std::vector<std::string> answer(seen.begin(), seen.end());
        std::sort(answer.begin(), answer.end());
        return answer;
    }
};
