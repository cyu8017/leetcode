// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

#include <string>
#include <unordered_map>

class FileSystem {
public:
    FileSystem() { paths[""] = -1; }

    bool createPath(std::string path, int value) {
        if (paths.count(path)) return false;
        auto pos = path.rfind('/');
        std::string parent = path.substr(0, pos);
        if (!paths.count(parent)) return false;
        paths[path] = value;
        return true;
    }

    int get(std::string path) {
        auto it = paths.find(path);
        return it == paths.end() ? -1 : it->second;
    }

private:
    std::unordered_map<std::string, int> paths;
};
