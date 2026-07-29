// LeetCode 0911 - Online Election
// https://leetcode.com/problems/online-election/

#include <algorithm>
#include <unordered_map>
#include <vector>

class TopVotedCandidate {
public:
    TopVotedCandidate(std::vector<int>& persons, std::vector<int>& times) : times_(times) {
        std::unordered_map<int, int> counts;
        int leader = -1;
        leaders_.resize(persons.size());
        for (int i = 0; i < (int)persons.size(); i++) {
            counts[persons[i]]++;
            if (leader == -1 || counts[persons[i]] >= counts[leader]) {
                leader = persons[i];
            }
            leaders_[i] = leader;
        }
    }

    int q(int t) {
        int i = (int)(std::upper_bound(times_.begin(), times_.end(), t) - times_.begin()) - 1;
        return leaders_[i];
    }

private:
    std::vector<int> times_;
    std::vector<int> leaders_;
};
