// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

#include <queue>
#include <set>
#include <unordered_map>
#include <vector>

class FileSharing {
public:
    FileSharing(int m) : next_id_(1) {}

    int join(std::vector<int> ownedChunks) {
        int user;
        if (!free_.empty()) {
            user = free_.top();
            free_.pop();
        } else {
            user = next_id_++;
        }
        chunks_[user] = std::set<int>(ownedChunks.begin(), ownedChunks.end());
        for (int chunk : ownedChunks) {
            owners_[chunk].insert(user);
        }
        return user;
    }

    void leave(int userID) {
        auto it = chunks_.find(userID);
        if (it != chunks_.end()) {
            for (int chunk : it->second) {
                owners_[chunk].erase(userID);
            }
            chunks_.erase(it);
        }
        free_.push(userID);
    }

    std::vector<int> request(int userID, int chunkID) {
        std::vector<int> users(owners_[chunkID].begin(), owners_[chunkID].end());
        if (!users.empty()) {
            chunks_[userID].insert(chunkID);
            owners_[chunkID].insert(userID);
        }
        return users;
    }

private:
    std::unordered_map<int, std::set<int>> owners_;
    std::unordered_map<int, std::set<int>> chunks_;
    std::priority_queue<int, std::vector<int>, std::greater<int>> free_;
    int next_id_;
};
