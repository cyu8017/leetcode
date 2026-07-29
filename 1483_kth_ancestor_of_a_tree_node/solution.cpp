#include <vector>

class TreeAncestor {
    std::vector<std::vector<int>> up;
public:
    TreeAncestor(int n, std::vector<int>& parent) {
        int width = 1;
        while ((1 << width) <= n) ++width;
        up.assign(width, std::vector<int>(n, -1));
        up[0] = parent;
        for (int b = 1; b < width; ++b)
            for (int i = 0; i < n; ++i) {
                int p = up[b - 1][i];
                up[b][i] = p == -1 ? -1 : up[b - 1][p];
            }
    }

    int getKthAncestor(int node, int k) {
        int bit = 0;
        while (k && node != -1) {
            if (k & 1) {
                if (bit >= (int)up.size()) return -1;
                node = up[bit][node];
            }
            ++bit;
            k >>= 1;
        }
        return node;
    }
};
