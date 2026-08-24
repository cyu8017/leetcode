// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

class Matrix3D(private val n: Int) {
    private val m: Array<Array<IntArray>> = Array(n) { Array(n) { IntArray(n) } }
    private val ones = IntArray(n)

    fun setCell(x: Int, y: Int, z: Int) {
        if (m[x][y][z] == 0) {
            m[x][y][z] = 1
            ones[x] = ones[x] + 1
        }
    }

    fun unsetCell(x: Int, y: Int, z: Int) {
        if (m[x][y][z] == 1) {
            m[x][y][z] = 0
            ones[x] = ones[x] - 1
        }
    }

    fun largestMatrix(): Int {
        var best = -1
        var idx = 0
        for (i in 0 until n) {
            if (ones[i] >= best) {
                best = ones[i]
                idx = i
            }
        }
        return idx
    }
}
