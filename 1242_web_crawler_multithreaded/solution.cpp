// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

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
        std::vector<std::string> frontier{startUrl};
        while (!frontier.empty()) {
            std::vector<std::string> nextFrontier;
            for (const std::string& url : frontier) {
                for (const std::string& next : htmlParser->getUrls(url)) {
                    if (hostOf(next) == host && !seen.count(next)) {
                        seen.insert(next);
                        nextFrontier.push_back(next);
                    }
                }
            }
            frontier.swap(nextFrontier);
        }
        std::vector<std::string> answer(seen.begin(), seen.end());
        std::sort(answer.begin(), answer.end());
        return answer;
    }
};
