// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

#include <algorithm>
#include <set>
#include <vector>

class ExamRoom {
public:
    ExamRoom(int n) : n_(n) {}

    int seat() {
        if (seats_.empty()) {
            seats_.insert(0);
            return 0;
        }
        int bestSeat = 0;
        int bestDist = *seats_.begin();
        auto it = seats_.begin();
        int prev = *it;
        for (++it; it != seats_.end(); ++it) {
            int dist = (*it - prev) / 2;
            if (dist > bestDist) {
                bestDist = dist;
                bestSeat = prev + dist;
            }
            prev = *it;
        }
        if (n_ - 1 - *seats_.rbegin() > bestDist) {
            bestSeat = n_ - 1;
        }
        seats_.insert(bestSeat);
        return bestSeat;
    }

    void leave(int p) { seats_.erase(p); }

private:
    int n_;
    std::set<int> seats_;
};
