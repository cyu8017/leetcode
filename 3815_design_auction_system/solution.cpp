// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

class AuctionSystem {
    struct Bid {
        int amount;
        int userID;
        bool operator<(const Bid& o) const {
            if (amount != o.amount) return amount < o.amount;
            return userID < o.userID;
        }
    };
    std::unordered_map<int, std::unordered_map<int, int>> bids;
    std::unordered_map<int, std::priority_queue<Bid>> heaps;

public:
    AuctionSystem() {}

    void addBid(int userId, int itemId, int bidAmount) {
        bids[itemId][userId] = bidAmount;
        heaps[itemId].push({bidAmount, userId});
    }

    void updateBid(int userId, int itemId, int newAmount) {
        addBid(userId, itemId, newAmount);
    }

    void removeBid(int userId, int itemId) {
        bids[itemId].erase(userId);
    }

    int getHighestBidder(int itemId) {
        auto it = heaps.find(itemId);
        if (it == heaps.end()) return -1;
        auto& h = it->second;
        while (!h.empty()) {
            Bid top = h.top();
            auto bit = bids[itemId].find(top.userID);
            if (bit != bids[itemId].end() && bit->second == top.amount) return top.userID;
            h.pop();
        }
        return -1;
    }
};
