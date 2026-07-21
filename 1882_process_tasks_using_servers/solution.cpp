// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

#include <algorithm>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<int> assignTasks(std::vector<int>& servers, std::vector<int>& tasks) {
        using Server = std::pair<int, int>;
        using Busy = std::tuple<long long, int, int>;
        std::priority_queue<Server, std::vector<Server>, std::greater<Server>> available;
        for (int i = 0; i < static_cast<int>(servers.size()); i++) {
            available.push({servers[i], i});
        }
        std::priority_queue<Busy, std::vector<Busy>, std::greater<Busy>> busy;
        std::vector<int> answer;
        long long time = 0;

        for (int moment = 0; moment < static_cast<int>(tasks.size()); moment++) {
            time = std::max(time, static_cast<long long>(moment));
            while (!busy.empty() && std::get<0>(busy.top()) <= time) {
                auto [finishTime, weight, index] = busy.top();
                busy.pop();
                available.push({weight, index});
            }
            while (available.empty()) {
                time = std::get<0>(busy.top());
                while (!busy.empty() && std::get<0>(busy.top()) <= time) {
                    auto [finishTime, weight, index] = busy.top();
                    busy.pop();
                    available.push({weight, index});
                }
            }
            auto [weight, index] = available.top();
            available.pop();
            busy.push({time + tasks[moment], weight, index});
            answer.push_back(index);
        }
        return answer;
    }
};
