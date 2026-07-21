// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

#include <unordered_map>
#include <vector>

class FindSumPairs {
public:
    FindSumPairs(std::vector<int>& nums1, std::vector<int>& nums2)
        : nums1_(nums1), nums2_(nums2) {
        for (int num : nums2_) {
            counts_[num]++;
        }
    }

    void add(int index, int val) {
        counts_[nums2_[index]]--;
        nums2_[index] += val;
        counts_[nums2_[index]]++;
    }

    int count(int tot) {
        int answer = 0;
        for (int num : nums1_) {
            auto it = counts_.find(tot - num);
            if (it != counts_.end()) {
                answer += it->second;
            }
        }
        return answer;
    }

private:
    std::vector<int> nums1_;
    std::vector<int> nums2_;
    std::unordered_map<int, int> counts_;
};
