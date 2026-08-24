// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

class ExamRoom(private val n: Int) {
    private val seats = TreeSet<Int>()

    fun seat(): Int {
        if (seats.isEmpty()) {
            seats.add(0)
            return 0
        }
        var bestSeat = 0
        var bestDist = seats.first()
        var prev = seats.first()
        for (cur in seats) {
            if (cur == prev) continue
            val dist = (cur - prev) / 2
            if (dist > bestDist) {
                bestDist = dist
                bestSeat = prev + dist
            }
            prev = cur
        }
        if (n - 1 - seats.last() > bestDist) bestSeat = n - 1
        seats.add(bestSeat)
        return bestSeat
    }

    fun leave(p: Int) {
        seats.remove(p)
    }
}
