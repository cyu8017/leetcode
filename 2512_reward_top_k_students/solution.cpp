// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

#include <algorithm>
#include <sstream>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> topStudents(std::vector<std::string>& positive_feedback,
                                 std::vector<std::string>& negative_feedback,
                                 std::vector<std::string>& report,
                                 std::vector<int>& student_id, int k) {
        std::unordered_set<std::string> pos(positive_feedback.begin(), positive_feedback.end());
        std::unordered_set<std::string> neg(negative_feedback.begin(), negative_feedback.end());
        std::vector<std::pair<int, int>> arr(report.size());
        for (int i = 0; i < (int)report.size(); i++) {
            int score = 0;
            std::istringstream iss(report[i]);
            std::string w;
            while (iss >> w) {
                if (pos.count(w)) score += 3;
                else if (neg.count(w)) score--;
            }
            arr[i] = {student_id[i], score};
        }
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) {
            if (a.second != b.second) return a.second > b.second;
            return a.first < b.first;
        });
        std::vector<int> ans(k);
        for (int i = 0; i < k; i++) ans[i] = arr[i].first;
        return ans;
    }
};
