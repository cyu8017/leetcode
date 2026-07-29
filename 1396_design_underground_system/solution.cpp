#include <string>
#include <unordered_map>
#include <utility>

class UndergroundSystem {
    std::unordered_map<int, std::pair<std::string, int>> ins;
    std::unordered_map<std::string, std::pair<long long, int>> stats;
    static std::string key(const std::string& a, const std::string& b) { return a + ">" + b; }
public:
    UndergroundSystem() {}

    void checkIn(int id, std::string stationName, int t) {
        ins[id] = {stationName, t};
    }

    void checkOut(int id, std::string stationName, int t) {
        auto [start, begin] = ins[id];
        ins.erase(id);
        auto& [total, count] = stats[key(start, stationName)];
        total += t - begin;
        ++count;
    }

    double getAverageTime(std::string startStation, std::string endStation) {
        auto [total, count] = stats[key(startStation, endStation)];
        return (double)total / count;
    }
};
