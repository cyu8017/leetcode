// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char, unordered_set<char>> graph;
        unordered_map<char, int> indegree;

        for (const string& word : words) {
            for (char ch : word) {
                graph.emplace(ch, unordered_set<char>());
                indegree.emplace(ch, 0);
            }
        }

        for (size_t i = 0; i + 1 < words.size(); i++) {
            const string& first = words[i];
            const string& second = words[i + 1];
            if (first.size() > second.size() && first.rfind(second, 0) == 0) {
                return "";
            }
            size_t limit = min(first.size(), second.size());
            for (size_t j = 0; j < limit; j++) {
                char left = first[j];
                char right = second[j];
                if (left != right) {
                    if (!graph[left].count(right)) {
                        graph[left].insert(right);
                        indegree[right]++;
                    }
                    break;
                }
            }
        }

        queue<char> q;
        for (const auto& entry : indegree) {
            if (entry.second == 0) {
                q.push(entry.first);
            }
        }

        string order;
        while (!q.empty()) {
            char ch = q.front();
            q.pop();
            order.push_back(ch);
            for (char next : graph[ch]) {
                if (--indegree[next] == 0) {
                    q.push(next);
                }
            }
        }

        return order.size() == indegree.size() ? order : "";
    }
};
